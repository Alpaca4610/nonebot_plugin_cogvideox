from pydantic import Extra, BaseModel


class Config(BaseModel, extra=Extra.ignore):
    zhipu_key: str = ""  # （必填）智谱清言清影API KEY
    video_model: str = "cogvideox-flash" # 视频模型，cogvideox-flash免费
    video_quality: str = "quality"  # 输出模式，"quality"为质量优先，"speed"为速度优先
    video_size: str = "1920x1080"  # 视频分辨率，支持最高4K（如: "3840x2160"）
    video_fps : str = 30  # 帧率，可选为30或60


class ConfigError(Exception):
    pass