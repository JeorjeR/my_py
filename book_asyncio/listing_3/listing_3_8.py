import asyncio
from asyncio import AbstractEventLoop, CancelledError
import socket
import logging


async def echo(connection: socket,
               loop: AbstractEventLoop) -> None:
    try:
        while data := await loop.sock_recv(connection, 1024):
            if data == b'r':
                raise Exception('Неожиданная ошибка сети')
            await loop.sock_sendall(connection, data=b' -> '+data + b'\n\r')
    except CancelledError as e:
        logging.exception(e)
    finally:
        connection.close()


async def listen_for_connections(server_socket: socket,
                                 loop: AbstractEventLoop):
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f'Получен запрос на подключение от {address}')
        asyncio.create_task(echo(connection, loop))


async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ('127.0.0.1', 8000)

    server_socket.bind(server_address)
    server_socket.setblocking(False)

    server_socket.listen()

    await listen_for_connections(server_socket, asyncio.get_event_loop())


if __name__ == '__main__':
    asyncio.run(main())
