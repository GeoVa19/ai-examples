from classes import Graph

graph = Graph()

graph.edges = {
    'A' : [ 'B' ],
    'B' : [ 'C', 'G' ],
    'C' : [ 'D' ],
    'D' : [ 'E', 'G' ],
    'E' : [],
    'F' : [ 'H' ],
    'G' : [],
    'H' : [ 'I' ],
    'I' : [ 'J' ],
    'J' : [ 'G' ],
    'K' : [ 'L' ],
    'L' : [],
    'S' : [ 'A', 'F', 'K' ]
}

weights = {
    ('A', 'B') : 2,
    ('B', 'C') : 2,
    ('B', 'G') : 3,
    ('C', 'D') : 2,
    ('D', 'E') : 1,
    ('D', 'G') : 5,
    ('S', 'A') : 2,
    ('S', 'F') : 1,
    ('S', 'K') : 2,
    ('F', 'H') : 1,
    ('H', 'I') : 1,
    ('I', 'J') : 1,
    ('J', 'G') : 1,
    ('K', 'L') : 1
}

# with respect to node G
heuristic = {
    'A' : 2,
    'B' : 3,
    'C' : 4,
    'D' : 5,
    'E' : 6,
    'F' : 4,
    'G' : 0,
    'H' : 3,
    'I' : 2,
    'J' : 1,
    'K' : 5,
    'L' : 6,
    'S' : 4
}
