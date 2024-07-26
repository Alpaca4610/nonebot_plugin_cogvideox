<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-chatgpt-turbo
</div>

# 介绍
- 本插件适配智谱清言的cogvideox视频生成模型API，具有文字生成视频和图文生成视频的功能。
# 安装

* 手动安装
  ```
  git clone https://github.com/Alpaca4610/nonebot_plugin_cogvideox.git
  ```

  下载完成后在bot项目的pyproject.toml文件手动添加插件：

  ```
  plugin_dirs = ["xxxxxx","xxxxxx",......,"下载完成的插件路径/nonebot_plugin_cogvideox.git"]
  ```
* 使用 pip
  ```
  pip install nonebot-plugin-cogvideox.git
  ```

# 配置文件

在Bot根目录下的.env文件中追加如下内容：

```
zhipu_key = ""  # （必填）智谱清言清影API KEY
```
[API KEY获取地址](https://open.bigmodel.cn/usercenter/apikeys)
# 效果
![](demo1.jpg)
![](demo2.jpg)

# 使用方法

- AI视频 文字提示词(图片)
