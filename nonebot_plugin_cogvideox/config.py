from pydantic import Extra, BaseModel


class Config(BaseModel, extra=Extra.ignore):
    zhipu_key: str = ""  # （必填）智谱清言清影API KEY


class ConfigError(Exception):
    pass