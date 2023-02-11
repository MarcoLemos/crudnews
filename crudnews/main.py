import uvicorn
from fastapi import FastAPI

from .routers.articles import router as articles_router

app = FastAPI()


@app.get('/health', tags=['health'])
async def health_check():
    return {'status': 'ok'}


app.include_router(articles_router)


if __name__ == '__main__':
    uvicorn.run(app)
