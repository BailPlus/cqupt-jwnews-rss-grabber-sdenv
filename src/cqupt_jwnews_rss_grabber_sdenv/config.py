from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    SDENV_SERVER_URL: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


config = Config()
