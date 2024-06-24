import datetime
from typing import Annotated

from annotated_types import MaxLen, MinLen

from pydantic import BaseModel, ConfigDict, EmailStr


class UserM(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    password: Annotated[str, MinLen(6), MaxLen(18)]
    email: EmailStr
    created: datetime.datetime


class UserCreateM(BaseModel):
    name: str
    password: Annotated[str, MinLen(6), MaxLen(18)]
    email: EmailStr
