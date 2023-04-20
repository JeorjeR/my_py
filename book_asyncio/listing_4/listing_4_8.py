import asyncio

import aiohttp

from util import MY_SERVER_URL
from util.decorators import async_timed
from util.fetch import fetch_status, fetch_text


@async_timed
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [fetch_text(session, MY_SERVER_URL) for _ in range(1000)]
        for finished_task in asyncio.as_completed(fetchers):
            print(await finished_task)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
