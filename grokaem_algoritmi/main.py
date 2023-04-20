import time
from random import randint

from alg import quicksort

lst = [randint(1, 2100) for i in range(100_000_000)]

s = time.perf_counter()
list(quicksort(lst))
e = time.perf_counter()
print(f'TIME {e-s}')


states_needed = {['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az']}
stations = {
    'kone': {['id', 'nv', 'ut']},
    'ktwo': {['wa', 'id', 'mt']},
    'kthree': {['or', 'nv', 'ca']},
    'kfour': {['nv', 'ut']},
    'kfive': {['ca', 'az']},
}
final_stations = set()
best_station = None
states_covered = set()
for station, states_for_station in stations.items():
    covered = states_needed & states_for_station
    if len(covered) > len(states_covered):
        best_station = station
        states_covered = covered

