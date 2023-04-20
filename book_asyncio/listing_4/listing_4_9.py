import asyncio

import aiohttp

from util import MY_SERVER_URL
from util.decorators import async_timed
from util.fetch import fetch_status


@async_timed
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [fetch_status(session, MY_SERVER_URL) for _ in range(1000)]
        for done_task in asyncio.as_completed(fetchers, timeout=2):
            try:
                result = await done_task
                print(result)
            except asyncio.TimeoutError:
                print('ЭХААЙ БАЛЯ Произошел тайм айт')

        for task in asyncio.tasks.all_tasks():
            print(task)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
