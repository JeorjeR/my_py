import asyncio

from util.decorators import async_timed
from aiohttp import ClientSession


@async_timed
async def fetch_status(session: ClientSession, url: str, delay=0) -> int:
    await asyncio.sleep(delay)
    async with session.get(url) as result:
        return result.status


@async_timed
async def fetch_text(session: ClientSession, url: str) -> str:
    async with session.get(url) as result:
        return await result.text()
