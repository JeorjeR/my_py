import asyncio
import asyncpg

from listing_5.connect import CONNECT_SETTING
from listing_5.queryes import PRODUCT_QUERY
from util.decorators import async_timed


async def query_product(pool):
    async with pool.acquire() as connection:
        return await connection.fetchrow(PRODUCT_QUERY)


@async_timed
async def query_products_synchronously(pool, queries):
    return [await query_product(pool) for _ in range(queries)]


@async_timed
async def query_products_concurrently(pool, queries):
    queries = [query_product(pool) for _ in range(queries)]
    return await asyncio.gather(*queries)


async def main():
    async with asyncpg.create_pool(**CONNECT_SETTING, min_size=6, max_size=6) as pool:

        await query_products_synchronously(pool, 100_000)
        await query_products_concurrently(pool, 100_000)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
