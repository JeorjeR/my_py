import asyncio
from util.delay_functions import delay
from util.decorators import async_timed


@async_timed
async def main() -> None:
    delay_times = [3, 3, 3]
    tasks = [asyncio.create_task(delay(seconds)) for seconds in delay_times]
    [await task for task in tasks]


if __name__ == '__main__':
    asyncio.run(main())
