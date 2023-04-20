import logging

import asyncio

from listing_5.connect import connect


async def main():
    connection = await connect()

    async with connection.transaction():
        await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'my_new_brand')")

        try:
            async with connection.transaction():
                await connection.execute("INSERT INTO product_color VALUES(1, 'black')")
        except Exception as ex:
            logging.warning('Ошибка при вставке цвета товара игнорируется', exc_info=ex)


if __name__ == '__main__':
    asyncio.run(main())
