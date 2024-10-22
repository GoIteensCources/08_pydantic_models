import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from settings import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[str] = mapped_column()
    create_date: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    age: Mapped[int]
    role: Mapped[str] = mapped_column()


class UserDetails(Base):
    __tablename__ = "userdetails"

    id: Mapped[int] = mapped_column(primary_key=True)

    phone_number: Mapped[str] = mapped_column()

    date_birth: Mapped[str] = mapped_column()

    country: Mapped[str] = mapped_column()


