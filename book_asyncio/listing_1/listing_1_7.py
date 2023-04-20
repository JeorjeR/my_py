import time
from urllib import request


def read_example() -> None:
    time.sleep(10)
    # with request.urlopen('https://vk.com') as response:
    #     print(response.read().decode('utf-8'))

if __name__ == '__main__':
    sync_start = time.time()

    read_example()
    read_example()

    sync_end = time.time()

    print(f'Синхронное выполнение заняло{sync_end - sync_start:.4f} c.')
