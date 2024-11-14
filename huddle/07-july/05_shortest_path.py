'''
05. Camino más corto: Dado un grafo pequeño con 5 nodos y 6 aristas, escribe una función 
que encuentre el camino más corto entre dos nodos especificados usando cualquier método que prefieras.
'''

from collections import deque

graph = { 
    '0': ['1', '2'], 
    '1': ['3', '4'], 
    '2': ['4'],
    '3': [],
    '4': []
} 

def bfs(graph, start, end):
    visited = set()
    queue = deque([[start]])
    
    if start == end:
        return [start]
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node not in visited:
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                
                if neighbor == end:
                    return new_path
            visited.add(node)
    
    return None

path = bfs(graph, '0', '4')

print("->".join(path))

