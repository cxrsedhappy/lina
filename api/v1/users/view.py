from fastapi import APIRouter, Depends, HTTPException, status

from core.models import create_session

from .auth import get_current_user
from .schemas import UserCreateM, UserM
from . import crud

router = APIRouter(prefix='/user', tags=['Users'])


@router.post('', status_code=status.HTTP_201_CREATED, response_model=UserM)
async def create_users(user: UserCreateM, session=Depends(create_session)):
    return await crud.create_user(session, user)


@router.get('', response_model=list[UserM])
async def get_users(session=Depends(create_session)):
    return await crud.get_users(session)


@router.get('/me', response_model=UserM)
async def get_me(user=Depends(get_current_user), session=Depends(create_session)):
    return await crud.get_users_by_id(session, user['id'])


@router.get('/{user_id}', response_model=UserM)
async def get_user(user_id: int, session=Depends(create_session)):
    user = await crud.get_users_by_id(session, user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User id:{user_id} not found'
        )

    return user
