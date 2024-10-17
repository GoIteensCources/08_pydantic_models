import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from routes.users import route as route_user
from settings import settings_app

app = FastAPI()


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse("/docs")


@app.get("/settings", tags=["tools"])
async def settings_rout():
    return settings_app


app.include_router(route_user, prefix="/users", tags=["user"])

if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", reload=True)
