import asyncio
import logging

import aiohttp

from util import MY_SERVER_URL
from util.decorators import async_timed
from util.fetch import fetch_status


@async_timed
async def main():
    async with aiohttp.ClientSession() as session:
        good_request = fetch_status(session, MY_SERVER_URL)
        bad_request = fetch_status(session, 'boom/'+MY_SERVER_URL)
        fetchers = [
            asyncio.create_task(good_request),
            asyncio.create_task(bad_request)
        ]
        done, pending = await asyncio.wait(fetchers)

        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число завершившихся задач: {len(pending)}')

        for done_task in done:
            # result = await done_task Возбудит исключение
            if exc := done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error(
                    'При выполнении запроса возникло исключение',
                    exc_info=exc
                )


if __name__ == '__main__':
    asyncio.run(main())
