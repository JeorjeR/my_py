import asyncio
from asyncpg import Connection
from asyncpg.cursor import Cursor

from listing_5.connect import connect


async def main():
    connection: Connection = await connect()
    async with connection.transaction():
        query = 'SELECT product_id, product_name from product'
        cursor: Cursor = await connection.cursor(query)
        await cursor.forward(500)
        products = await cursor.fetch(100)
        for product in products:
            print(product)
    await connection.close()


if __name__ == '__main__':
    asyncio.run(main())


