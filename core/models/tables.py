from __future__ import annotations

import datetime

from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    is_email_verified: Mapped[bool] = mapped_column(default=False)
    created: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.utcnow())

    def __init__(self, username, password, email, **kwargs):
        self.username = kwargs.get('username', username)
        self.hashed_password = kwargs.get('password', password)
        self.email = kwargs.get('email', email)

    def __repr__(self):
        return f'<User id={self.id} name={self.username} email={self.email}>'
