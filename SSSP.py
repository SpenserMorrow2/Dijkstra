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

#usage test (real graph to be placed here)
graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}

source = 0
shortest_paths = dijkstra(graph, source)
print(shortest_paths)
