import collections
import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def neighbors(self, name):
        return self.edges[name]

class Queue:
    def __init__(self):
        self.items = collections.deque()

    def empty(self):
        return len(self.items) == 0

    def put(self, x):
        self.items.append(x)

    def get(self):
        return self.items.popleft()

# min-heap
class PriorityQueue:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def put(self, item, priority):
        heapq.heappush(self.items, (priority, item))

    def get(self):
	# returns the item with the highest priority
        return heapq.heappop(self.items)[1]
