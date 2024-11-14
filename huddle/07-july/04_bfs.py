# 04. Recorrido en amplitud (BFS): Implementa un recorrido BFS para un grafo simple con 5 nodos.

graph = {
    '1' : ['2', '3'],
    '2' : ['4'],
    '3' : ['5'],
    '4' : [],
    '5' : []
}

def bfs(graph, node):
    q = []
    visited = set()

    q.append(node)
    visited.add(node)

    while q:
        currentNode = q.pop(0)

        print(currentNode)

        for neighbor in graph[currentNode]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)

bfs(graph, '1')