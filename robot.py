def first_t(sequence):
    sequence = sorted(sequence)
    return sequence.index('T')

def split(sequence):
    c_list = []
    for i in sequence: c_list.append(i)
    return c_list

def walk(sequence, cont, value):
    if not sequence: return 0
    if cont < len(sequence):
        if sequence[cont] == 'F': return walk(sequence, cont + 1, value + 1)
        else: return walk(sequence, cont + 1, value - 1)
    else: return value

def walk_2(sequence):
    if not sequence: return 0
    else:
        if sequence.pop() == 'F': return walk_2(sequence) + 1
        else: return walk_2(sequence) - 1

while True:
    print('1. Recursivo\n2. Iterativo\n3. Recursivo 2\n0. Break')
    choice = input('>>')

    if choice == '1':
        sequence = input("Digite o comando do robo: ").upper()
        sequence = split(sequence)
        valor = walk(sequence, 0, 0)         # Conta recursivamente quantos T's e quantos F's existem na lista e retorna essa diferença.
        print('O robô andou: '+ str(valor))

    elif choice == '2':
        sequence = input("Digite o comando do robo: ").upper()
        index_t = first_t(sequence)                 # O index_t não é apenas o index do primeiro T como também é a quantidade de F existentes na lista ( quando ela esta ordenada )
        qtd = index_t - (len(sequence) - index_t)   # (len(sequence) - index_t) é a quantidade de T's que existem na lista.
        print('O ROBO ANDOU: '+str(qtd))

    elif choice == '3':
        sequence = input("Digite o comando do robo: ").upper()
        sequence = list(sequence)
        qtd = walk_2(sequence)
        print('O ROBO ANDOU: ' + str(qtd))

    else: break

