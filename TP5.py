import numpy as np
import sys

def create_adjacency_matrix(edges, vertices):
    """Create adjacency matrix from edge list"""
    # Get unique vertices if not provided
    if not vertices:
        vertices = set()
        for s, e, _ in edges:
            vertices.add(s)
            vertices.add(e)
        vertices = sorted(list(vertices))
    
    # Create vertex to index mapping
    vertex_to_idx = {vertex: idx for idx, vertex in enumerate(vertices)}
    
    # Initialize matrix with infinity
    n = len(vertices)
    matrix = np.full((n, n), float('inf'))
    
    # Fill diagonal with zeros
    np.fill_diagonal(matrix, 0)
    
    # Fill matrix with weights
    for start, end, weight in edges:
        i, j = vertex_to_idx[start], vertex_to_idx[end]
        matrix[i][j] = weight
    
    return matrix, vertices, vertex_to_idx

def dijkstra(graph, source_idx, target_idx, vertices):
    """Implementation of Dijkstra's algorithm"""
    n = len(vertices)
    dist = [float('inf')] * n
    prev = [None] * n
    visited = [False] * n
    
    dist[source_idx] = 0
    
    for _ in range(n):
        # Find minimum distance vertex
        min_dist = float('inf')
        min_vertex = -1
        
        for v in range(n):
            if not visited[v] and dist[v] < min_dist:
                min_dist = dist[v]
                min_vertex = v
        
        if min_vertex == -1:
            break
            
        visited[min_vertex] = True
        
        # Update distances
        for v in range(n):
            if (not visited[v] and 
                graph[min_vertex][v] != float('inf') and 
                dist[min_vertex] + graph[min_vertex][v] < dist[v]):
                dist[v] = dist[min_vertex] + graph[min_vertex][v]
                prev[v] = min_vertex
    
    # Reconstruct path
    path = []
    current = target_idx
    
    while current is not None:
        path.append(vertices[current])
        current = prev[current]
    
    path.reverse()
    
    return path, dist[target_idx]

def main():
    # Define edges
    edges = [
        ('A','C',1), ('A','B',4), ('C','F',7), ('B','F',3),
        ('C','D',8), ('D','H',5), ('F','H',1), ('F','E',1),
        ('E','H',2), ('H','G',3), ('H','M',7), ('H','L',6),
        ('G','L',4), ('E','L',2), ('G','M',4), ('L','M',1)
    ]
    
    # Get unique vertices
    vertices = sorted(list(set([v for edge in edges for v in edge[:2]])))
    
    # Create adjacency matrix
    matrix, vertices, vertex_to_idx = create_adjacency_matrix(edges, vertices)
    
    # Get user input
    source = input("Enter source vertex: ")
    target = input("Enter target vertex: ")
    
    # Validate input
    if source not in vertices or target not in vertices:
        print("Invalid vertices!")
        return
    
    # Find shortest path
    path, total_weight = dijkstra(
        matrix,
        vertex_to_idx[source],
        vertex_to_idx[target],
        vertices
    )
    
    # Print results
    print(f"\nShortest path from {source} to {target}:")
    print(" -> ".join(path))
    print(f"Total weight: {total_weight}")

if __name__ == "__main__":
    main()