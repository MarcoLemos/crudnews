import pytest
from httpx import AsyncClient


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


@pytest.mark.anyio
async def test_get_article(client: AsyncClient):
    response = await client.get('/articles')
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    if response.json():
        assert isinstance(response.json()[0]['title'], str)
