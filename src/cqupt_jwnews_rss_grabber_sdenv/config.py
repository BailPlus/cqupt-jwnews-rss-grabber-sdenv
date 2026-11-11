from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings, **SettingsConfigDict(env_file=".env", extra="ignore")):
    SDENV_SERVER_URL: str
    SDENV_SERVER_CA_FILE: Path | bool = True


config = Config()
