def dijkstra(graph, first, last):

    distances = {}
    unvisited = []
    prev = {}
    path = []

    path.append(first)
    cur_v = last

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

    while cur_v != first:
        try:
            path.append(cur_v)
            cur_v = prev[cur_v]
        except KeyError:
            print('Path not avaliable.')
            break

    if distances[last] != float("inf"):
        return distances[last], path


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

'''
g = {1: [(2, 10), (3,2)],
     2: [(1, 10), (3, 15)],
     3: [(2, 15), (4, 12),(1,2)],
     4: [(3, 12)]
    }

o = int(4)
d = int(2)
print(dijkstra(g, o, d))
'''
