import uvicorn
from fastapi import FastAPI


app = FastAPI()

@app.get('/health')
async def health_check():
    return {'status': 'ok'}

if __name__ == '__main__':
    uvicorn.run(app)