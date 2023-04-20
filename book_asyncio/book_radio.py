import asyncio
import dataclasses
from asyncio import AbstractEventLoop
import socket
from util.decorators import async_timed


class AsyncFileIter:

    def __init__(self, data):
        self.data = iter(data)

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            value = next(self.data)
        except StopIteration:
            raise StopAsyncIteration
        return value


class AsyncReader:

    def __init__(self, data: str, line: int):
        line = line if line in (0, 1) else line - 2
        self.data = data.split('\n')[line:]

    def __aiter__(self):
        return AsyncFileIter(self.data)


def read_file(file_name):
    return open(file_name, encoding='windows-1251').read()


@dataclasses.dataclass
class User:
    address: str
    line: int

    def __repr__(self):
        return f'User({self.address!r}, {self.line})'


users_data: list[User] = []


@async_timed
async def echo(connection: socket,
               user: User,
               loop: AbstractEventLoop) -> None:
    try:
        data = await loop.run_in_executor(None, read_file, 'text.txt')
        row: str
        async for row in AsyncReader(data, user.line):
            user.line += 1
            await asyncio.sleep(5)
            await loop.sock_sendall(connection, row.encode() + b'\n\r')
    except ConnectionAbortedError:
        user.line -= 1
        print(f'Пользователь {user.address} разорвал соединение')
        print(f'{len(asyncio.all_tasks())}')
    finally:
        connection.close()


@async_timed
async def listen_for_connections(server_socket: socket,
                                 loop: AbstractEventLoop):
    while True:
        connection, address = await loop.sock_accept(server_socket)
        try:
            user: User = next(user for user in users_data if user.address == address[0])
        except StopIteration:
            users_data.append(user := User(address[0], 0))
        print(user)
        connection.setblocking(False)
        print(f'Получен запрос на подключение от {address}')
        asyncio.create_task(echo(connection, user, loop))


@async_timed
async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ('10.0.0.237', 8000)

    server_socket.bind(server_address)
    server_socket.setblocking(False)

    server_socket.listen()
    loop = asyncio.get_event_loop()

    await listen_for_connections(server_socket, loop)


if __name__ == '__main__':
    asyncio.run(main())
