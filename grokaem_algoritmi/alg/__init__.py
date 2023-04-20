

def _find_smallest(arr) -> int:
    smallest = arr[0]
    smallest_index = 0
    for index, el in enumerate(arr[1:], start=1):
        if el < smallest:
            smallest = el
            smallest_index = index
    return smallest_index


def binary_search(obj_: list | tuple, item) -> int | None:
    low = 0
    high = len(obj_) - 1

    while low <= high:
        mid = low + high
        guess = obj_[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


def selection_sort(arr: list):
    arr_ = arr[:]
    for i in range(len(arr_)):
        smallest_index = _find_smallest(arr_)
        yield arr_.pop(smallest_index)


def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        mid = len(arr) // 2
        pivot = arr[mid]
        arr_ = arr[:mid] + arr[mid+1:]
        less = [el for el in arr_ if el <= pivot]
        greater = [el for el in arr_ if el > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


def depth_first_search(graph, data, func):
    from collections import deque
    search_queue = deque()
    search_queue.extend(graph[data])
    searched = []
    while search_queue:
        element = search_queue.popleft()
        if element not in searched:
            if func(element):
                return True
        else:
            search_queue.extend(graph[element])
            searched.append(element)
    return False
# Белман-Форд

graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['in'] = None


# def deykstra():
#     processed = []
#     node = find_lowest_cost_node(costs)
#     while node is not None:
#         cost = cost[node]
#         neighbors = graph[node]
#         for n in neighbors.keys():
#             new_cost = cost + neighbors[n]
#             if costs[n] > new_cost:
#                 costs[n] = new_cost
#                 parents[n] = node
#         processed.append(node)
#         node = find_lowest_cost_node(costs)


