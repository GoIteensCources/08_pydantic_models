import asyncio

from models import User, UserDetails
from settings import engine, Base, async_session
from werkzeug.security import generate_password_hash

async def create_bd():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def insert_data():
    async with async_session() as sess:
        u1 = User(name="admin",
                  age=18,
                  email="afmin@ex.com",
                  password_hash=generate_password_hash("admin"),
                  role="admin", )
        u1_det = UserDetails(phone_number="+380661515172",
                             date_birth="01.01.2000",
                             country="Ua",
                             user=u1)

        sess.add(u1)
        sess.add(u1_det)
        await sess.commit()


async def main():
    await create_bd()
    print("database created")
    await insert_data()
    print("data added")
    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())

