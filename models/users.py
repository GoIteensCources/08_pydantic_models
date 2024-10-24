from datetime import datetime

from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from settings import Base
from schemas.users import UserType


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[str] = mapped_column()
    age: Mapped[int]
    role: Mapped[UserType] = mapped_column()

    create_date: Mapped[datetime] = mapped_column(server_default=func.now())
    user_details = relationship('UserDetails',
                                back_populates='user',
                                cascade="all, delete-orphan")

    def __str__(self):
        return f"User: {self.email}, {self.role}"


class UserDetails(Base):
    __tablename__ = "user_details"

    id: Mapped[int] = mapped_column(primary_key=True)
    phone_number: Mapped[str] = mapped_column()
    date_birth: Mapped[str] = mapped_column()
    country: Mapped[str] = mapped_column()

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='user_details')


