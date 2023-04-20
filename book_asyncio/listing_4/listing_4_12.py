import asyncio
import logging
from collections import deque

import aiohttp

from util import MY_SERVER_URL
from util.decorators import async_timed
from util.fetch import fetch_status


@async_timed
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = deque([
            fetch_status(session, MY_SERVER_URL) for _ in range(2)
        ])
        fetchers.appendleft(asyncio.create_task(fetch_status(session, 'boom/'+MY_SERVER_URL)))

        done, pending = await asyncio.wait(fetchers,
                                           return_when=asyncio.FIRST_EXCEPTION)

        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')

        done_task: asyncio.Task
        for done_task in done:
            if exc := done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error(
                    'При выполнении запроса возникло исключение',
                    exc_info=exc
                )
            pending_task: asyncio.Task
            for pending_task in pending:
                pending_task.cancel()
        

if __name__ == '__main__':
    asyncio.run(main())
