import asyncio as asyncio

from listing_5.connect import connect
from listing_5.queryes import CREATE_BRAND_TABLE, CREATE_PRODUCT_TABLE, CREATE_PRODUCT_COLOR_TABLE, \
    CREATE_PRODUCT_SIZE_TABLE, CREATE_SKU_TABLE, SIZE_INSERT, COLOR_INSERT


async def main():
    connection = await connect()

    statements = (
        CREATE_BRAND_TABLE,
        CREATE_PRODUCT_TABLE,
        CREATE_PRODUCT_COLOR_TABLE,
        CREATE_PRODUCT_SIZE_TABLE,
        CREATE_SKU_TABLE,
        SIZE_INSERT,
        COLOR_INSERT
    )

    print('Создается база данных product...')

    for statement in statements:
        status = await connection.execute(statement)
        print(status)
    print('База данных product создана!')
    await connection.close()


if __name__ == '__main__':
    asyncio.run(main())




