import os
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = 'crudnews-backend'
    mongo_username: str
    mongo_password: str
    db_name: str
    environment: str

    class Config:
        env_file = os.path.expanduser('.env')


@lru_cache()
def get_settings():
    return Settings()
