import asyncio
import aiohttp
from aiohttp import ClientSession

from util import MY_SERVER_URL
from util.decorators import async_timed
from util.fetch import fetch_status


@async_timed
async def main():
    async with aiohttp.ClientSession() as session:
        url = MY_SERVER_URL
        async with session.get(url) as response:
            status = await fetch_status(session, url)
            text = await response.text()
        print(f'Состояние для {url} было равно {status}, текст {text}')

if __name__ == '__main__':
    asyncio.run(main())
