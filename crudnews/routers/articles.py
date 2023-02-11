from typing import List

from fastapi import APIRouter, HTTPException
from odmantic import ObjectId

from crudnews.db import engine
from crudnews.models.articles_models import Articles

router = APIRouter(
    prefix='/articles',
    tags=['articles'],
    responses={404: {'description': 'Not found'}},
)


@router.get('', response_model=List[Articles])
async def get_articles():
    articles = await engine.find(Articles)
    return articles


@router.get('/count', response_model=int)
async def count_articles():
    count = await engine.count(Articles)
    return count


@router.get('/{id}', response_model=Articles)
async def get_article_by_id(id: ObjectId):
    article = await engine.find_one(Articles, Articles.id == id)
    if article is None:
        raise HTTPException(404)
    return article


@router.post('', response_model=Articles)
async def create_article(articles: Articles):
    await engine.save(articles)
    return articles


@router.delete('/{id}', response_model=Articles)
async def delete_article_by_id(id: ObjectId):
    article = await engine.find_one(Articles, Articles.id == id)
    if article is None:
        raise HTTPException(404)
    await engine.delete(article)
    return article
