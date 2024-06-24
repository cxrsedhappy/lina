from __future__ import annotations

import datetime

from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    created: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.utcnow())

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.password = kwargs.get('password')
        self.email = kwargs.get('email')

    def __repr__(self):
        return f'<User id={self.id} name={self.name} email={self.email}>'
