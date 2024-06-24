import uvicorn

from fastapi import FastAPI, Body
from pydantic import BaseModel, EmailStr


class CreateUserM(BaseModel):
    email: EmailStr


app = FastAPI(
    title='Todos',
    version='0.0.1'
)

items = ['item1', 'item2', 'item3']


@app.get('/')
async def index():
    return {'msg': 'hello world'}


@app.get('/items')
async def list_items():
    return items


@app.post('/user')
async def create_user(user: CreateUserM):
    return user.email


@app.get('/items/{item_id}')
async def get_item_by_id(item_id: int):
    return items[item_id]


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
