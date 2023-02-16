import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

from .routers.articles import router as articles_router
from .routers.exception_handlers import (
    http_exception_handler,
    server_error_handler,
    validation_exception_handler,
)

app = FastAPI()


origins = [
    '*'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/health', tags=['health'])
async def health_check():
    return {'status': 'ok'}


app.include_router(articles_router)

app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, server_error_handler)

if __name__ == '__main__':
    uvicorn.run(app)
