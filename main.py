import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from routes.users import route as route_user
from routes.tasks import route as route_task

app = FastAPI()


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse("/docs")


app.include_router(route_user, prefix="/users")
# app.include_router(route_task, prefix="/tasks")

if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", reload=True)
