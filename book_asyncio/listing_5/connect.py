import asyncpg


CONNECT_SETTING = dict(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        database='products1',
        password='root',
)


async def connect():
    connection = await asyncpg.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        database='products1',
        password='root',
    )
    return connection
