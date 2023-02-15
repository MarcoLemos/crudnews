from os import environ

from fastapi import HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

from crudnews.config import get_settings

DB_NAME = 'localhost'
USR = get_settings().mongo_username
PASSW = get_settings().mongo_password

container_env = environ.get('CONTAINER', False)

if container_env:
    DB_NAME = get_settings().db_name


def get_engine():
    uri = f'mongodb://{USR}:{PASSW}@{DB_NAME}:27017/'

    try:
        client = AsyncIOMotorClient(uri, serverSelectionTimeoutMS=5000)
        connection = AIOEngine(client=client, database='crudnews')
        return connection
    except (ConnectionFailure, ServerSelectionTimeoutError) as exc:
        raise HTTPException(
            status_code=500, detail='Erro de conexão com o banco de dados'
        ) from exc


engine = get_engine()
