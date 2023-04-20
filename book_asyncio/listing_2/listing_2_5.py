import asyncio


async def hello_world_message() -> str:
    await asyncio.sleep(4)
    return 'Hello World!'


async def main() -> None:
    message = await hello_world_message()
    print(message)

if __name__ == '__main__':
    asyncio.run(main())
