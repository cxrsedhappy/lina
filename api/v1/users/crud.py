from typing import Sequence

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import User
from .schemas import UserCreateM


async def create_user(session: AsyncSession, _user: UserCreateM):
    user = User(**_user.model_dump())
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


async def get_users(session: AsyncSession) -> Sequence[User]:
    statement = select(User).order_by(User.id)
    result: Result = await session.execute(statement)
    users = result.scalars().all()
    return users


async def get_users_by_id(session: AsyncSession, user_id) -> User | None:
    return await session.get(User, user_id)
