import asyncio
from asyncpg import Connection

from listing_5.connect import connect


async def main():
    connection: Connection = await connect()
    query = 'SELECT product_id, product_name FROM product'
    async with connection.transaction():
        async for product in connection.cursor(query):
            print(product)
    await connection.close()


if __name__ == '__main__':
    asyncio.run(main())


