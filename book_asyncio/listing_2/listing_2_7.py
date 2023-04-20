import asyncio

from listing_2_2 import coroutine_add_one
from util.delay_functions import delay


async def hello_world_message() -> str:
    await delay(1)
    return 'Hello World!'


async def main() -> None:
    message = await hello_world_message()
    one_plus_one = await coroutine_add_one(1)
    print(one_plus_one)
    print(message)

if __name__ == '__main__':
    asyncio.run(main())
