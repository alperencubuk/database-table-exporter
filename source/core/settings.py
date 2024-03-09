from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_TITLE: str = "Exporter"
    VERSION: str = "1.0.0"
    DATABASE_URIS: dict = {}
    broker_url: str = "redis://redis:6379/0"
    result_backend: str = "redis://redis:6379/1"


settings = Settings()
