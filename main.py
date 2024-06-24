from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from api.v1 import router as router_v1

from core.models import global_init


@asynccontextmanager
async def lifespan(app: FastAPI):
    await global_init()
    yield


app = FastAPI(title='Todos', version='0.0.1', lifespan=lifespan)
app.include_router(router_v1)


@app.get('/')
async def index():
    return {'msg': 'hello world'}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
