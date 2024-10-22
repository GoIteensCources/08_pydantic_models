import datetime

import nullable
from sqlalchemy import func, ForeignKey
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
    userdetails = relationship('UserDetails', back_populates='users')

class UserDetails(Base):
    __tablename__ = "userdetails"

    id: Mapped[int] = mapped_column(primary_key=True)

    phone_number: Mapped[str] = mapped_column()

    date_birth: Mapped[str] = mapped_column()

    country: Mapped[str] = mapped_column()

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='userdetails')


