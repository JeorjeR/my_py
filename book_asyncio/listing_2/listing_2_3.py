import asyncio

from listing_2_2 import coroutine_add_one


if __name__ == '__main__':
    result = asyncio.run(coroutine_add_one(1))
    print(result)
