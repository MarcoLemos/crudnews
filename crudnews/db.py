from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from os import environ
from crudnews.config import get_settings

DB_NAME = 'localhost'
USR = get_settings().mongo_username
PASSW = get_settings().mongo_password

container_env = environ.get('CONTAINER', False)

if container_env:
    DB_NAME = get_settings().db_name

def get_engine():
    uri = f'mongodb://{USR}:{PASSW}@{DB_NAME}:27017/'
    client = AsyncIOMotorClient(uri)
    connection = AIOEngine(client=client, database='crudnews')
    return connection


engine = get_engine()
