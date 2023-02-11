from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine

from crudnews.config import get_settings

USR = get_settings().mongo_username
PASSW = get_settings().mongo_password


def get_engine():
    uri = f'mongodb://{USR}:{PASSW}@localhost:27017/admin'
    client = AsyncIOMotorClient(uri)
    connection = AIOEngine(client=client, database='crudnews')
    return connection


engine = get_engine()
