def thePath(origin, current, destiny, path, distance, prev):

    if current != origin:

        path.append(current)
        current = prev[current]

        return thePath(origin, current, destiny, path, distance, prev)

    else:

        path.append(origin)
        if distance[destiny] != float("inf"):
            return distance[destiny], path[::-1]


def recCalculatePath(adj_list, min_vert, prev, distance, count):

    if count < len(adj_list):

        min_path = distance[min_vert] + adj_list[count][1]

        if min_path < distance[adj_list[count][0]]:

            distance[adj_list[count][0]] = min_path
            prev[adj_list[count][0]] = min_vert

        recCalculatePath(adj_list, min_vert, prev, distance, count + 1)

def recDijkstra(graph, origin, destiny, distance, unvisited, prev, path):

    if not unvisited:

        current = destiny
        return thePath(origin, current, destiny, path, distance, prev)

    else:

        min_vert = min(unvisited, key=lambda vertex: distance[vertex])
        adj_list = graph[min_vert]
        recCalculatePath(adj_list, min_vert, prev, distance, 0)

        unvisited.remove(min_vert)
        return recDijkstra(graph, origin, destiny, distance, unvisited, prev, path)

def dijkstra(graph, origin, destiny):

    distance = {}
    unvisited = []
    prev = {}
    path = []

    for v in graph:

        distance[v] = float("inf")
        unvisited.append(v)

    distance[origin] = 0

    paths = recDijkstra(graph, origin, destiny, distance, unvisited, prev, path)

    return paths

def main():

    v, origin, destiny = [int(n) for n in input().split()]
    graph = {list: [] for list in range(1, v + 1)}

    # Cria um grafo do tipo "{1: [(2, 10)], 2: [(1, 10), (3, 11)], etc... }"
    # onde a chave é o vertice e seus elementos são (adjacente, custo)
    for i in range(v - 1):
        v1, v2, cost = [int(n) for n in input().split()]

        graph[v1].append((v2, cost))
        graph[v2].append((v1, cost))

    print(dijkstra(graph, origin, destiny))

g = {1: [(2, 10), (3,2)],
     2: [(1, 10), (3, 15)],
     3: [(2, 15), (4, 12),(1,2)],
     4: [(3, 12)]
    }

o = int(4)
d = int(2)
print(dijkstra(g, o, d))

#print(dijkstra(g, o, d))