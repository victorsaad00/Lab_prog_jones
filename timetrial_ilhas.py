def dijkstra(graph, ilha, servidor):

    distances = {}
    unvisited = []
    prev = {}
    path = []

    for v in graph:

        distances[v] = float("inf")
        unvisited.append(v)

    distances[ilha] = 0

    while unvisited:

        min_v = min(unvisited, key=lambda vertex: distances[vertex])

        for v in graph[min_v]:

            min_path = distances [min_v] + v[1]

            if min_path < distances[v[0]]:

                distances[v[0]] = min_path
                prev[v[0]] = min_v

        unvisited.remove(min_v)


'''

A ideia era calcular o valor do ping de todas as ilhas existentes até a ilha do servidor.
Com a ajuda do algoritmo de dijkstra, o ping seria calculado e o resultado do ping daquela ilha até o servidor
seria salvo em uma lista de pings. Depois, com todos os pings salvos, iria pegar o menor e o maior valor dos pings
e subtrair o maior do menor retornando o resultado. O calculo do maior e menor valor poderia ser feito atavés da ordenação
da lista de pings, e pegaria o primeiro e o ultimo valor ( mas seria mais custuoso ) ou poderia ser utilizado a
função min e max da biblioteca do python. tambem retornando esse valor. 

'''
def main():

    N, M = [int(n) for n in input().split()]

    ilhas = {list: [] for list in range(1, N + 1)}
    distance = {}
    servidor = int(0)

    # Não deu tmepo ed fazer a entrada certa.
    for i in range(N):
        U, V, ping = [int(n) for n in input().split()]

        ilhas[U].append((V, ping))
        ilhas[V].append((U, ping))
        ilhas[U].append((V, ping))

    ilha = []
    for i in ilhas:
        ilha.append(i) # todos as ilhas


    resultados = []
    for v in ilha:
        resultados.append(dijkstra(ilhas, v, servidor))





main()
