import asyncio
import logging
from asyncio import AbstractEventLoop
import socket
import signal
from typing import List

from util.exception import GracefulExit, shutdown


async def echo(connection: socket, loop: AbstractEventLoop) -> None:
    try:
        while data := await loop.sock_recv(connection, 1024):
            print('got data')
            if data == b'boom\r\n':
                raise Exception('Неожиданная ошибка сети')
            await loop.sock_sendall(connection, data)
    except Exception as ex:
        logging.exception(ex)
    finally:
        connection.close()


async def connection_listener(server_socket: socket, loop: AbstractEventLoop):
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f'Получено сообщение от {address}')
        echo_task = asyncio.create_task(echo(connection, loop))
        echo_tasks.append(echo_task)


async def close_echo_tasks(echo_tasks: List[asyncio.Task]):
    waiters = [asyncio.wait_for(task, 2) for task in echo_tasks]
    for task in waiters:
        try:
            await task
        except TimeoutError:
            pass


async def main():
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ('127.0.0.1', 8000)
    server_socket.bind(server_address)
    server_socket.setblocking(False)
    server_socket.listen()

    for signame in {'SIGINT', 'SIGTERM'}:
        loop.add_signal_handler(getattr(signal, signame), shutdown)

    await connection_listener(server_socket, loop)


if __name__ == '__main__':
    echo_tasks = []
    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(main())
    except GracefulExit:
        loop.run_until_complete(close_echo_tasks(echo_tasks))
    finally:
        loop.close()

