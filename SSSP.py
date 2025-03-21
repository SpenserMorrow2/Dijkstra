import heapq

"""
    Implements Dijkstra's algorithm using a binary min heap.
    
    Parameters:
    - graph: dict, adjacency list where graph[u] = [(v, weight), ...]
    - source: int, starting vertex
    
    Returns:
    - distances: dict, shortest distances from source to each vertex
"""

def dijkstra(graph, source):
    distances = {node: float('inf') for node in graph} # init dists; source 0, inf for the rest
    distances[source] = 0
    
    pq = [(0, source)] #use min heap storing (dist, vert)
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]: #ignore if popped dist > stored
            continue
        
        for neighbor, weight in graph[current_vertex]: #relaxation
            distance = current_distance + weight
            if distance < distances[neighbor]: 
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances


graph = {
    1: [(2, 1), (10, 2), (11, 1)],
    2: [(1, 1), (3, 1), (21, 2)],
    3: [(2, 1), (4, 1), (8, 2)],
    4: [(3, 1), (5, 1)],
    5: [(4, 1), (6, 2), (7, 1), (22, 1)],
    6: [(5, 2), (7, 1)],
    7: [(5, 1), (6, 1), (8, 1)],
    8: [(3, 2), (7, 1), (9, 1)],
    9: [(8, 1), (10, 1), (19, 1)],
    10: [(9, 1), (11, 1), (1, 2), (18, 2)],
    11: [(10, 1), (12, 2), (1, 1), (17, 1)],
    12: [(11, 2), (13, 2)],
    13: [(12, 2), (14, 2), (21, 1)],
    14: [(13, 2), (15, 1), (16, 1), (20, 1)],
    15: [(14, 1)],
    16: [(14, 1), (17, 2)],
    17: [(16, 2), (18, 1), (11, 1)],
    18: [(17, 1), (19, 2), (10, 2)],
    19: [(18, 2), (9, 1)],
    20: [(14, 1), (21, 2), (22, 1)],
    21: [(20, 2), (13, 1), (22, 2), (2, 2)],
    22: [(21, 2), (5, 1), (20, 1)]
}


source = 1
shortest_paths = dijkstra(graph, source)
print(shortest_paths)
