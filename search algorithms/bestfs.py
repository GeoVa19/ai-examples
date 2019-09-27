from classes import Graph, Queue, PriorityQueue
from graph_init import graph, weights, heuristic

def bestfs(graph, start, goal):
    searchFrontier = PriorityQueue()
    searchFrontier.put(start, heuristic[start])
    predecessor = {}
    predecessor[start] = None

    path = ""

    while not searchFrontier.empty():
        current = searchFrontier.get()

        path += current + " "

        if current == goal:
            break

        for next in graph.neighbors(current):
            if next not in predecessor:
                priority = heuristic[next]
                searchFrontier.put(next, priority)
                predecessor[next] = current

    return path

print("Path with Best-First algorithm: ")
print(bestfs(graph, 'S', 'G'))
