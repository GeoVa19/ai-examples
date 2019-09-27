from classes import Graph, Queue, PriorityQueue
from graph_init import graph, weights, heuristic

def bfs(graph, start, goal):
    searchFrontier = Queue()
    searchFrontier.put(start)
    explored = {}
    explored[start] = True

    path = ""

    while not searchFrontier.empty():
        current = searchFrontier.get()

        path += current + " "

        if current == goal:
            break

        # for each neighbor node
        for next in graph.neighbors(current):
            if next not in explored:
                searchFrontier.put(next) # add none in the queue
                explored[next] = True

    return path

print("Path with BFS algorithm: ")
print(bfs(graph, 'S', 'G'))
