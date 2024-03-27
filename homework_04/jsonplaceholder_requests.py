import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def get_users_data() -> dict:
    data: dict = await fetch_json(USERS_DATA_URL)
    return data


async def get_posts_data() -> dict:
    data: dict = await fetch_json(POSTS_DATA_URL)
    return data
