import asyncio
import aiohttp
from aiohttp import ClientSession

from util import MY_SERVER_URL


async def fetch_status(session: ClientSession, url: str) -> int:
    ten_millis = aiohttp.ClientTimeout(total=.01)
    async with session.get(url, timeout=ten_millis) as result:
        return result.status


async def main():
    session_timeout = aiohttp.ClientTimeout(total=10, connect=.1)
    async with aiohttp.ClientSession(timeout=session_timeout) as session:
        await fetch_status(session, MY_SERVER_URL)


if __name__ == '__main__':
    asyncio.run(main())
    