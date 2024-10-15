from fastapi import APIRouter

route = APIRouter()

@route.post("/")
async def create():
    ...


@route.get("/")
async def get_all():
    ...


@route.get("/{id_task}")
async def get_by_id(id_task:int):
    ...
