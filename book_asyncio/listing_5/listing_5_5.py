from random import sample
from typing import Union

import asyncio

from listing_5.connect import connect


def load_common_words() -> list[str]:
    with open('common_words.txt', encoding='windows-1251') as common_words:
        return common_words.readlines()


def generate_brand_names(words: list[str]) -> list[tuple[Union[str, ]]]:
    return [(words[index], ) for index in sample(range(100), 100)]


async def insert_brands(common_words, connection) -> int:
    brands = generate_brand_names(common_words)
    insert_brands_ = 'INSERT INTO brand VALUES(DEFAULT, $1)'
    return await connection.executemany(insert_brands_, brands)


async def main():
    common_words = load_common_words()
    connection = await connect()
    await insert_brands(common_words, connection)


if __name__ == '__main__':
    asyncio.run(main())
