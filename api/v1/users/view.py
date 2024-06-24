from fastapi import APIRouter, Depends, HTTPException, status

from . import crud
from .schemas import UserCreateM, UserM
from core.models import create_session

router = APIRouter(tags=['Users'])


@router.post('', response_model=UserM)
async def create_users(user: UserCreateM, session=Depends(create_session)):
    return await crud.create_user(session, user)


@router.get('', response_model=list[UserM])
async def get_users(session=Depends(create_session)):
    return await crud.get_users(session)


@router.get('/{user_id}', response_model=UserM)
async def get_user(user_id: int, session=Depends(create_session)):
    user = await crud.get_users_by_id(session, user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User id:{user_id} not found'
        )

    return user
