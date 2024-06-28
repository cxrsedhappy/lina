import datetime
from typing import Annotated

from annotated_types import MaxLen, MinLen

from pydantic import BaseModel, ConfigDict, EmailStr


class UserM(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str
    hashed_password: str
    email: EmailStr
    is_email_verified: bool
    created: datetime.datetime


class UserCreateM(BaseModel):
    username: str
    password: Annotated[str, MinLen(6), MaxLen(18)]
    email: EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str
