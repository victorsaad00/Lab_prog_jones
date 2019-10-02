# Implementação de do algoritmo de Dijkstra.
def dijkstra(graph, first, last):

    distances = {}
    unvisited = []
    prev = {}
    path = []

    for v in graph:

        distances[v] = float("inf")
        unvisited.append(v)

    distances[first] = 0

    while unvisited:

        min_v = min(unvisited, key=lambda vertex: distances[vertex])

        for v in graph[min_v]:

            min_path = distances [min_v] + v[1]

            if min_path < distances[v[0]]:

                distances[v[0]] = min_path
                prev[v[0]] = min_v

        unvisited.remove(min_v)


    cur_v = last
    while cur_v is not first:
        try:

            path.append(cur_v)
            cur_v = prev[cur_v]

        except KeyError:

            print('Path not avaliable.')
            break

    path.append(first)
    if distances[last] != float("inf"):
        return distances[last], path[::-1]


def main():

    v, origin, destiny = [int(n) for n in input().split()]
    graph = {list: [] for list in range(1, v + 1)}

    # Cria um grafo do tipo "{1: [(2, 10)], 2: [(1, 10), (3, 11)], etc... }"
    # onde a chave é o vertice e seus elementos são (adjacente, custo)
    for i in range(v - 1):
        v1, v2, cost = [int(n) for n in input().split()]

        graph[v1].append((v2,cost))
        graph[v2].append((v1, cost))

    print(dijkstra(graph, origin, destiny))


g = {
    1:[(4,1),(5,1)],
    2:[(3,1),(8,2)],
    3:[(2,1),(4,1),(10,80),(9,70)],
    4:[(1,1),(3,1)],
    5:[(7,50),(1,1),(6,1)],
    6:[(5,1)],
    7:[(8,1),(5,50)],
    8:[(7,1),(2,2)],
    9:[(3,70)],
    10:[(3,80)]
}


print(dijkstra(g,7,6))

