import datetime as dt
from typing import Optional

from pydantic import BaseModel, Field, EmailStr, HttpUrl
import enum


class UserType(str, enum.Enum):
    USER = "user"
    ADMIN = "admin"


class UsersBase(BaseModel):
    name: str = Field(min_length=4)
    email: EmailStr
    password: str = Field(min_length=4)

    sign_up: dt.datetime = Field(dt.datetime.now())
    role_user: UserType = UserType.USER


class ListBaseUsers(BaseModel):
    users: list[UsersBase]
    count_users: int


class ForExtend(BaseModel):
    friends: list[int] = []
    website: Optional[HttpUrl] = None


class UsersExtended(UsersBase, ForExtend):
    ...
