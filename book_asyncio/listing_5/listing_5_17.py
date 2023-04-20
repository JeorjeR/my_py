import asyncio
from asyncpg import Connection

from listing_5.connect import connect


async def take(generator, to_take: int):
    item_count = 0
    async for item in generator:
        if item_count > to_take - 1:
            return
        item_count += 1
        yield item


async def main():
    connection: Connection = await connect()

    async with connection.transaction():
        query = 'SELECT product_id, product_name FROM product'
        product_generator = connection.cursor(query)
        async for product in take(product_generator, 5):
            print(product)
        print('Получены первые пять товаров')

    await connection.close()


if __name__ == '__main__':
    asyncio.run(main())

