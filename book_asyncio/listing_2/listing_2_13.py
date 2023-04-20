import asyncio
from util.delay_functions import delay


async def main():
    delay_task = asyncio.create_task(delay(10))
    try:
        result = await asyncio.wait_for(asyncio.shield(delay_task), 5)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Задача работает дольше 5 секунд, скоро она закончится')
        result = await delay_task
        print(result)

if __name__ == '__main__':
    asyncio.run(main())
