import asyncio

import aiohttp

from util import MY_SERVER_URL
from util.decorators import async_timed
from util.fetch import fetch_status


@async_timed
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [
            fetch_status(session, MY_SERVER_URL) for _ in range(10)
        ]

        done, pending = await asyncio.wait(fetchers, timeout=6)

        print(f'Число зарешившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')

        for done_task in done:
            result = await done_task
            print(result)


if __name__ == '__main__':
    asyncio.run(main())
