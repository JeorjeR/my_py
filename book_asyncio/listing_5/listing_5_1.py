import asyncio

import asyncpg


async def main():
    connection = await asyncpg.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        database='products1',
        password='root',
    )

    version = connection.get_server_version()
    print(f'Подключено! Версия Postgres равна {version}')
    await connection.close()


if __name__ == '__main__':
    asyncio.run(main())
