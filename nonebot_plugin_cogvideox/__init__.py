import asyncio
import time
import nonebot

from nonebot import on_command,get_plugin_config
from nonebot.params import CommandArg
from nonebot.log import logger
from nonebot.adapters.onebot.v11 import (
    Message,
    MessageSegment,
    MessageEvent,
    helpers
)

from zhipuai import ZhipuAI
from nonebot.plugin import PluginMetadata
from .config import Config, ConfigError

__plugin_meta__ = PluginMetadata(
    name="基于清影的AI视频生成",
    description="基于智谱清言清影cogvideox模型的AI视频生成nonebot插件，支持文生视频和图文生视频",
    usage="""
    AI视频 文字提示词(图片)
    """,
    config=Config,
    extra={},
    type="application",
    homepage="https://github.com/Alpaca4610/nonebot_plugin_cogvideox",
    supported_adapters={"~onebot.v11"},
)


plugin_config = get_plugin_config(Config)

if not plugin_config.zhipu_key:
    raise ConfigError("请配置AI视频生成的KEY")
api_key = plugin_config.zhipu_key
client = ZhipuAI(api_key=api_key)
model = "cogvideox"


def create_video_task(client, model, prompt, image_url):
    response = client.videos.generations(
        model=model, prompt=prompt, image_url=image_url
    )
    return response


def get_video_generation_result(client, task_id):
    response = client.videos.retrieve_videos_result(id=task_id)
    return response


def text_to_vid(prompt_text, img_url):
    text_task_response = create_video_task(client, model, prompt_text, img_url)
    text_task_id = text_task_response.id if hasattr(text_task_response, "id") else None
    if not text_task_id:
        logger.error(text_task_response)
        return False, "无法创建视频生成任务"

    print(f"Text-to-video task created with ID: {text_task_id}")
    while True:
        text_result_response = get_video_generation_result(client, text_task_id)
        text_task_status = (
            text_result_response.task_status
            if hasattr(text_result_response, "task_status")
            else "UNKNOWN"
        )
        if text_task_status == "SUCCESS":
            logger.success("Text-to-video generation successful!")
            return True, text_result_response.video_result[0].url
        elif text_task_status == "FAIL":
            logger.error("Text-to-video generation failed!")
            return False, "视频生成失败"
        else:
            logger.info("Text-to-video generation still processing...")
            time.sleep(10)


genvid = on_command("AI视频", block=False, priority=1)


@genvid.handle()
async def _(event: MessageEvent, msg: Message = CommandArg()):
    content = msg.extract_plain_text()
    img_url = helpers.extract_image_urls(event.message)
    if content == "" or content is None:
        await genvid.finish(MessageSegment.text("内容不能为空！"), at_sender=True)
    if not img_url:
        img_url = [None]
    await genvid.send(MessageSegment.text("清影正在生成视频中......"), at_sender=True)
    try:
        loop = asyncio.get_event_loop()
        flag, res = await loop.run_in_executor(None, text_to_vid, content, img_url[0])
    except Exception as error:
        await genvid.finish(str(error), at_sender=True)
    if flag:
        await genvid.send(MessageSegment.text("视频播放链接："+res))
        await genvid.finish(MessageSegment.video(res))
    else:
        await genvid.finish(MessageSegment.text(res))
