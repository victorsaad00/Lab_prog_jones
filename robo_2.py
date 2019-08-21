def first_t(sequence):
    sequence = sorted(sequence)
    return sequence.index('T')



while True:
    print('1. Opção 1\n2. Opção 2\n0. Break')
    choice = input('>>')
    if choice == '1':
        sequence = input("Digite o comando do robo: ").upper()
        sequence = sorted(sequence)


    elif choice == '2':

        sequence = input("Digite o comando do robo: ").upper()
        index_t = first_t(sequence)
        qtd = index_t - (len(sequence) - index_t)
        if qtd == 0: print('A sequencia não altera a posição do robõ.')
        else: print('O robô andou : ' + str(qtd))

    else: break
