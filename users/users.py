from typing import Annotated

from fastapi import APIRouter, Path


router = APIRouter(tags=['Users'], prefix='/user')

db = {
    1: 'user1',
    2: 'user2',
    3: 'user3'
}


@router.get('')
async def get_users():
    return db


@router.get('/{user_id}')
async def get_user_by_id(user_id: Annotated[int, Path(ge=1, le=3)]):
    return db.get(user_id, '0')
