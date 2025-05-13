# project/app/config.py 

import logging
from functools import lru_cache

from pydantic_settings import BaseSettings 

log = logging.getLogger("uvicorn")

class Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = bool(0)

@lru_cache()
def get_settings():
    log.info("Loading config settings from then environment ...")
    return Settings()
