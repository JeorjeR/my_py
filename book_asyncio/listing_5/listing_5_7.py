import asyncio

import asyncpg

from listing_5.connect import CONNECT_SETTING
from listing_5.queryes import PRODUCT_QUERY


async def product_query(pool):
    async with pool.acquire() as connection:
        result = await connection.fetchrow(PRODUCT_QUERY)
        print(result)
        return result


async def main():
    async with asyncpg.create_pool(**CONNECT_SETTING,
                                   min_size=6,
                                   max_size=6) as pool:
        await asyncio.gather(
            product_query(pool),
            product_query(pool),
        )


if __name__ == '__main__':
    asyncio.run(main())

