from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.users import UserBase, InputUserData, FullUserBase, UserBaseDetails, ListBaseUsers

from models import User, UserDetails
from settings import get_session
from werkzeug.security import generate_password_hash

route = APIRouter()


@route.post("/")
async def create_registration(data_user: InputUserData,
                              session: AsyncSession = Depends(get_session)) -> UserBase:
    user_dict = data_user.model_dump()
    user_dict["password_hash"] = generate_password_hash(user_dict["password"])
    del user_dict["password_repeat"]
    del user_dict["password"]

    new_user = User(**user_dict)

    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)

    return UserBase.model_validate(new_user)


@route.get("/read/all/")
async def get_all_users(session: AsyncSession = Depends(get_session)) -> ListBaseUsers:
    users = await session.scalars(select(User))
    count = await session.scalar(select(func.count()).select_from(User))
    return ListBaseUsers(users=users, count_users=count)


@route.get("/{id_user}")
async def get_by_id(id_user: int, session: AsyncSession = Depends(get_session)) -> FullUserBase | UserBase:
    user = await session.get(User, id_user)
    if not user:
        raise HTTPException(404, f"User {id_user} not found")
    details_user = user.user_details
    if details_user:
        return FullUserBase.model_validate(user)
    return UserBase.model_validate(user)


@route.patch("/create/details/{id_user}")
async def create_extend_user(id_user: int,
                             data_ext: UserBaseDetails,
                             session: AsyncSession = Depends(get_session)) -> FullUserBase:
    user = await session.get(User, id_user)
    if not user:
        raise HTTPException(404, f"User {id_user} not found")
    user_det = UserDetails(phone_number=data_ext.phone_number,
                           date_birth=data_ext.date_birth,
                           country=data_ext.country,
                           user=user)
    session.add(user_det)
    await session.commit()
    await session.refresh(user)

    return FullUserBase.model_validate({**user.__dict__, "user_details": user_det})
    # return FullUserBase.model_validate(user)


@route.delete("/{id_user}", status_code=200)
async def delete_user(id_user: int, session: AsyncSession = Depends(get_session)):
    user = await session.get(User, id_user)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    await session.delete(user)
    await session.commit()
    return {"mess": f"{id_user} deleted"}
