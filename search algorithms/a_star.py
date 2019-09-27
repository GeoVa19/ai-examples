from classes import Graph, Queue, PriorityQueue
from graph_init import graph, weights, heuristic

def a_star_search(graph, start, goal):
    searchFrontier = PriorityQueue()
    searchFrontier.put(start, heuristic[start])
    currentCost = {}
    currentCost[start] = 0

    path = ""

    while not searchFrontier.empty():
        current = searchFrontier.get()

        # add node in path
        path += current + " "

        if current == goal:
            break

        for next in graph.neighbors(current):
            newCost = currentCost[current] + weights[(current, next)]
            if next not in currentCost or newCost < currentCost[next]:
                currentCost[next] = newCost
                priority = newCost + heuristic[next] # set priority
                searchFrontier.put(next, priority) # add node in priority queue

    return path

print("Path with A* algorithm: ")
print(a_star_search(graph, 'S', 'G'))
