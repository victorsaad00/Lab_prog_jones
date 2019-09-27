def printGraph(graph, col_graph):
    print('grafo = {' )
    for v in graph:
        print('    ' + str( v ) + ' : ' + str(graph[v]) + ' -> ' + str(col_graph[v]))
    print('}')

def createGraph(graph):

    print('Digite a quantidade de vertices do grafo ou zero para sair')
    v = int(input('>>'))

    for i in range(v):

        '''
            A entrada do grafo 'A' = ['B','C'] 
            seria A B C. E assim para os demais
            vertices. O primeiro elemento da lista 
            representa o vertice e os demais 
            representam os vertices adjacentes ao 
            primeiro elemento da lista solicitada.
            
        '''

        print('Digite os vertices: ')

        grafo = input('>>').split()

        vertice = grafo[0]
        grafo = grafo[1:]

        graph[vertice] = grafo

    return graph


def amountOfColorsUsed(col_graph):
    return len(set(col_graph.values()))

# Pega os vertices do grafo e coloca em uma lista
def getVertices(graph):

    vertices = []

    for v in graph:
        vertices.append(v)

    return vertices

# Recebe um vertice, uma cor, o grafo de vertices ja pintado e o grafo
# Assim, verifica se o vertice v ( o vertice do grafo ) ja tem cor no col_graph
# e os seus adjacentes

def paintGraph(v, color, col_graph, graph):

    for adj in graph.get(v):

        cor_vertice = col_graph.get(adj)

        if cor_vertice == color: return False

    return True

# Pega um vertice, uma cor e chama a funcao paintGraph
# Se paintGraph retornar verdade, a funcao retorna a cor
def getColors(vertice, colors, col_graph, graph):

    for c in colors:
        if paintGraph(vertice, c, col_graph, graph):
            return c

# Com a cor da funcao getColors, eh ligado o vertice v a uma cor no grafo
# col_graph representa um vertice pintado
def main():

    graph = {}
    col_graph = {}  # Grafo que vai relacionar vertice a sua cor.
    colors = ['Vermelho', 'Preto', 'Azul', 'Verde']

    graph = createGraph(graph)

    # Lista de vertices
    vertices = getVertices(graph)

    for v in vertices:
        col_graph[v] = getColors(v, colors, col_graph, graph)


    printGraph(graph, col_graph)

    print(' ---------------- ')
    print('O minimo de cores para pinta-lo foi: '+ str(amountOfColorsUsed(col_graph)))


main()
#Exmplo pratico de um grafo para preencher
'''
graph = {
    'a' : ['b', 'c', 'd', 'e', 'f'],
    'b' : ['a', 'c'],
    'c' : ['a', 'b', 'd', 'e', 'f', 'g'],
    'd' : ['a', 'c'],
    'e' : ['a', 'c', 'g', 'f'],
    'f' : ['a', 'g', 'e'],
    'g' : ['c', 'e', 'f'],
}

'''






