# 03. Recorrido en profundidad (DFS): Implementa un recorrido DFS para un grafo simple con 5 nodos.

graph = {
    '1': ['2', '3'],
    '2': ['4'],
    '3': ['5'],
    '4': [],
    '5': []
}

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
        
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

print("Depth-First Search")
dfs(graph, '1')
