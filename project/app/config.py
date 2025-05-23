# project/app/config.py

import logging
from functools import lru_cache

from pydantic import AnyUrl
from pydantic_settings import BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = bool(0)
    database_url: AnyUrl = None


@lru_cache()
def get_settings():
    log.info("Loading config settings from then environment ...")
    return Settings()
