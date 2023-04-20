import asyncio

from util.delay_functions import delay


async def main():
    results = await asyncio.gather(delay(3), delay(1))
    print(results)
    # Заглянуть в исходники gather и посмотреть реализацию через futures


if __name__ == '__main__':
    asyncio.run(main())

# 4.4.1 Обработка исключений при использовании gather
