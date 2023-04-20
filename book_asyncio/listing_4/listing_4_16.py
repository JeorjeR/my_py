import asyncio
from asyncio import Task

import aiohttp

from util import MY_SERVER_URL
from util.fetch import fetch_status


async def main():
    async with aiohttp.ClientSession() as session:
        api_a = asyncio.create_task(fetch_status(session, MY_SERVER_URL))
        api_b = asyncio.create_task(fetch_status(session, MY_SERVER_URL, delay=2))

        done, pending = await asyncio.wait([api_a, api_b], timeout=1)

        task: Task
        for task in pending:
            if task is api_b:
                print('API B слишком медленный, отмена')
                task.cancel()


if __name__ == '__main__':
    asyncio.run(main())
