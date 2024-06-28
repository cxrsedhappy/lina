from typing import Annotated

from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr
from annotated_types import MaxLen, MinLen


class UserM(BaseModel):
    """Main User model. Includes all data"""
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str
    hashed_password: str
    email: EmailStr
    is_email_verified: bool
    created: datetime


class UserCreateM(BaseModel):
    """User create model"""
    username: str
    password: Annotated[str, MinLen(6), MaxLen(18)]
    email: EmailStr


class TokenM(BaseModel):
    """Token model for OAuth"""
    access_token: str
    token_type: str
