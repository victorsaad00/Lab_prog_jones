def dijkstra(conexoes, ilha, servidor):

    pings = {}
    unvisited = []

    for v in conexoes:

        pings[v] = float("inf")
        unvisited.append(v)

    pings[ilha] = 0

    while unvisited:
        
        min_v = min(unvisited, key=lambda vertex: pings[vertex])
        for v in conexoes[min_v]:
            min_path = pings [min_v] + v[1]
            if min_path < pings[v[0]]:
                pings[v[0]] = min_path
                
        unvisited.remove(min_v)

    return pings[servidor]

def main():

    N, M = [int(n) for n in input().split()]
    conexoes = {list: [] for list in range(1, N + 1)}
    ilhas = []
    resultados = []

    for i in range(M):

        U, V, ping = [int(n) for n in input().split()]

        conexoes[U].append((V, ping))
        conexoes[V].append((U, ping))
        
        
    servidor = int(input())    

    for i in conexoes: ilhas.append(i)
        
    ilhas.remove(servidor)

    for v in ilhas:
        resultados.append(dijkstra(conexoes, v, servidor))

    min_ping, max_ping = min(resultados), max(resultados)
    print(str(max_ping - min_ping))

main()

'''

A ideia é calcular o valor do ping de todas as conexoes existentes até a ilha do servidor.
Com a ajuda do algoritmo de dijkstra, o ping seria calculado e o resultado do ping daquela ilhas até o servidor
seria salvo em uma lista de pings. Depois, com todos os pings salvos, iria pegar o menor e o maior valor dos pings
e subtrair o menos ping do maior ping retornando o resultado. Com a ajuda do min e max do python, podemos
calcular o maior e o menos ping e subtrair o menor do maior. Assim, obtendo o resultado desejado.

'''
