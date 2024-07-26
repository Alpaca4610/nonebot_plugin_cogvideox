from pydantic import Extra, BaseModel
from typing import Optional


class Config(BaseModel, extra=Extra.ignore):
    zhipu_key: Optional[str] = ""  # （必填）智谱清言清影API KEY


class ConfigError(Exception):
    pass