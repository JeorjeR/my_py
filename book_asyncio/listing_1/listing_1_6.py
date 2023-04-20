import threading
import time
from listing_1_5 import print_fib


def fibs_with_threads():
    first_thread = threading.Thread(target=print_fib, args=(40,))
    second_thread = threading.Thread(target=print_fib, args=(41,))

    first_thread.start()
    second_thread.start()

    first_thread.join()
    second_thread.join()

    start_threads = time.time()

    fibs_with_threads()

    end_threads = time.time()

    print(f'Многопоточное выполнение заняло {end_threads - start_threads:.4f} с.')
