import logging

import asyncio

from listing_5.connect import connect


async def main():
    connection = await connect()

    try:
        async with connection.transaction():
            insert_brand = "INSERT INTO brand VALUES(9999, 'big_brand')"
            await connection.execute(insert_brand)
            await connection.execute(insert_brand)
    except Exception:
        logging.exception('Ошибка выполнения транзакции')
    finally:
        query = """
            SELECT brand_name FROM brand
            WHERE brand_name LIKE 'big_%'
        """
        brands = await connection.fetch(query)
        print(f'Результат запроса: {brands}')


if __name__ == '__main__':
    asyncio.run(main())
