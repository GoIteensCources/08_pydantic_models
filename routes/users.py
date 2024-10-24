from fastapi import APIRouter

from schemas.users import UsersBase, ListBaseUsers, UsersExtended, ForExtend

route = APIRouter()

db = [UsersBase(name="Admin", email="admin@ex.com", password="passw", role_user="admin")
      ]

ext_db = []


@route.post("/")
async def create(data_user: UsersBase) -> UsersBase:
    db.append(data_user)
    return data_user


@route.get("/")
async def get_all() -> ListBaseUsers:
    return ListBaseUsers(users=db, count_users=len(db))


@route.get("/{id_user}")
async def get_by_id(id_user: int):
    ...


@route.patch("/extend/{id_user}")
async def extend(id_user: int, ext_data: ForExtend) -> UsersExtended:
    user = db[id_user].model_dump()
    return UsersExtended(**user, friends=ext_data.friends, website=ext_data.website)


@route.delete("/{id_user}")
async def delete_user(id_user: int):
    del db[id_user]
    return "deleted"
