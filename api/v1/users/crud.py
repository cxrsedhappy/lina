from typing import Sequence

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import User
from .schemas import UserCreateM
from .utils import bcrypt_context


async def create_user(session: AsyncSession, _user: UserCreateM):
    """
    Creates a new User.

    :param session: AsyncSession
    :param _user: UserCreateM
    :return: User object
    """
    dump = _user.model_dump()
    dump['password'] = bcrypt_context.hash(dump['password'])
    user = User(**dump)
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
