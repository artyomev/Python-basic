import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from homework_04.jsonplaceholder_requests import get_users_data, get_posts_data
from models import engine, Session
from models import User
from models import Post, Base


meta = Base.metadata


async def async_main():

    async with engine.begin() as conn:
        await conn.run_sync(meta.drop_all)
        await conn.run_sync(meta.create_all)


    async with Session()  as session:
        users_data, posts_data = await asyncio.gather(
            get_users_data(),
            get_posts_data(),
        )
        await create_users(session, users_data)
        await create_posts(session, posts_data)


async def create_users(
    session: AsyncSession,
    users_dict
) -> list[User]:

    users = [
        User(name=user_data['name'],
             username=user_data['username'],
             email=user_data['email']
             )
        for user_data in users_dict
    ]
    session.add_all(users)
    await session.commit()
    return users


async def create_posts(
    session: AsyncSession,
    posts_dict
) -> list[Post]:

    posts = [
        Post(title=post_data['title'],
             body=post_data['body'],
             user_id=post_data['userId']
             )
        for post_data in posts_dict
    ]
    session.add_all(posts)
    await session.commit()
    return posts


async def drop_create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(meta.drop_all)
        await conn.run_sync(meta.create_all)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
