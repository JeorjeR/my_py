import asyncio
import aiohttp
from aiohttp import ClientSession

from util import MY_SERVER_URL
from util.decorators import async_timed
from util.fetch import fetch_status


@async_timed
async def main():
    async with ClientSession() as session:
        urls = [MY_SERVER_URL for _ in range(100)]
        requests = [asyncio.create_task(fetch_status(session, url)) for url in urls]
        status_codes = await asyncio.gather(*requests)
        print(status_codes)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    