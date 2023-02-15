import pytest
from httpx import AsyncClient

@pytest.mark.anyio
async def test_get_article_by_id(client: AsyncClient):
    response = await client.post(
        '/articles',
        json={'title': 'Foo', 'content': 'foo bar'},
    )
    assert response.status_code == 200
    article_id = response.json()['id']

    response = await client.get(f'/articles/{article_id}')
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert response.json()['id'] == article_id


@pytest.mark.anyio
async def test_delete_article_by_id(client: AsyncClient):
    response = await client.post(
        '/articles',
        json={'title': 'Foo', 'content': 'foo bar'},
    )
    assert response.status_code == 200
    article_id = response.json()['id']

    response = await client.delete(f'/articles/{article_id}')
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert response.json()['id'] == article_id

    response = await client.get(f'/articles/{article_id}')
    assert response.status_code == 404


@pytest.mark.anyio
async def test_count_articles(client: AsyncClient):
    response = await client.get('/articles/count')
    assert response.status_code == 200
    assert isinstance(response.json(), int)
        
@pytest.mark.anyio
async def test_post_article(client: AsyncClient):
    response = await client.post(
        '/articles',
        json={'title': 'Foo', 'content': 'foo bar'},
    )
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    if response.json():
        assert isinstance(response.json()['title'], str)
        article_id = response.json()['id']
        response = await client.delete(f'/articles/{article_id}')


@pytest.mark.anyio
async def test_get_article(client: AsyncClient):
    response = await client.get('/articles')
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    if response.json():
        assert isinstance(response.json()[0]['title'], str)
