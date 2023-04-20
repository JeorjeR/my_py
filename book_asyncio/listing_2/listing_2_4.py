import asyncio
from listing_2_2 import coroutine_add_one


async def main() -> None:
    one_plus_one = await coroutine_add_one(1)
    two_plus_one = await coroutine_add_one(2)
    print(one_plus_one)
    print(two_plus_one)


if __name__ == '__main__':
    asyncio.run(main())
