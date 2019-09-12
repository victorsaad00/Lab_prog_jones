# Faz uma busca recursiva em todos os vertices do grafo
# Os que estão marcados como False, são passados para path
# sendo ( vertice, somatorio das arestas )
# Ao final, a tupla vertex é retornada
def recSearch(graph, vertex, last, visited, path):

    if vertex[0] == last:

        return vertex

    else:

        for v in graph[vertex[0]]:

            if visited[v[0]-1] is False:

                visited[v[0] - 1] = True
                path.append((v[0], v[1] + vertex[1]))

        return recSearch(graph, path.pop(0), last, visited, path)

# Marca os vertices "anteriores" adjacentes ao vertice de origem.
# Para que eles posteriormente não sejam contados.
def mark(graph, first, last, visited):

    path = []

    for v in graph[first]:

        path.append(v)
        visited[v[0]-1] = True

    vertix = path.pop(0)

    return recSearch(graph, vertix, last, visited, path)

def main():
    v, origin, destiny = [int(n) for n in input().split()]
    graph = {new_list: [] for new_list in range(1, v + 1)}

    # Cria um grafo do tipo "{1: [(2, 10)], 2: [(1, 10), (3, 11)], etc... }"
    # onde a chave é o vertice e seus elementos são (adjacente, custo)4 2
    for i in range(v - 1):
        v1, v2, cost = [int(n) for n in input().split()]

        graph[v1].append((v2,cost))
        graph[v2].append((v1, cost))

    visited = [False] * len(graph) # lista que relaciona os vertices visitados

    print(mark(graph,origin,destiny,visited)[1])

main()

