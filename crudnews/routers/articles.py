from typing import List

from fastapi import APIRouter, HTTPException
from odmantic import AIOEngine, ObjectId
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

from crudnews.db import engine
from crudnews.models.articles_models import Articles

router = APIRouter(
    prefix='/articles',
    tags=['articles'],
    responses={404: {'description': 'Not found'}},
)

CON_ERR = 'Erro de conexão com o banco de dados'


@router.get('', response_model=List[Articles])
async def get_articles():
    try:
        articles = await engine.find(Articles)
    except (ConnectionFailure, ServerSelectionTimeoutError) as exc:
        raise HTTPException(status_code=500, detail=CON_ERR) from exc
    return articles


@router.get('/count', response_model=int)
async def count_articles():
    try:
        count = await engine.count(Articles)
    except (ConnectionFailure, ServerSelectionTimeoutError) as exc:
        raise HTTPException(status_code=500, detail=CON_ERR) from exc
    return count


@router.get('/{id}', response_model=Articles)
async def get_article_by_id(id: ObjectId):
    try:
        article = await engine.find_one(Articles, Articles.id == id)
    except (ConnectionFailure, ServerSelectionTimeoutError) as exc:
        raise HTTPException(status_code=500, detail=CON_ERR) from exc
    if article is None:
        raise HTTPException(404)
    return article


@router.post('', response_model=Articles)
async def create_article(articles: Articles):
    try:
        await engine.save(articles)
    except (ConnectionFailure, ServerSelectionTimeoutError) as exc:
        raise HTTPException(status_code=500, detail=CON_ERR) from exc
    return articles


@router.delete('/{id}', response_model=Articles)
async def delete_article_by_id(id: ObjectId):
    try:
        article = await engine.find_one(Articles, Articles.id == id)
        if article is None:
            raise HTTPException(404)
        await engine.delete(article)
    except (ConnectionFailure, ServerSelectionTimeoutError) as exc:
        raise HTTPException(status_code=500, detail=CON_ERR) from exc
    return article
