import asyncio

from listing_5.connect import CONNECT_SETTING, connect


async def main():
    connection = await connect()

    async with connection.transaction():
        await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'brand_1')")
        await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'brand_2')")

        query = """
            SELECT brand_name FROM brand
            WHERE brand_name LIKE 'brand%'
        """
        brands = await connection.fetch(query)
        print(brands)

    await connection.close()


if __name__ == '__main__':
    asyncio.run(main())
