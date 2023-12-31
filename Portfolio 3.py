def sequencia_dna():
    lista = []
    mapeamento = str.maketrans({'1': 'A', '2': 'C', '3': 'G', '4': 'T'})

    while True:
        try:
            vezes = int(input('Quantos nucleotídeos deseja na sequência? '))
            break
        except ValueError:
            print('Por favor, digite um número inteiro válido.')

    while len(lista) < vezes:
        nucleotideo = input(f'Digite o {len(lista) + 1}° nucleotídeo de {vezes}: ')
        while nucleotideo not in ['1', '2', '3', '4']:
            print('Entrada inválida.')
            print('Nucleotídeos A, C, G e T correspondem respectivamente a 1, 2, 3 e 4.')
            nucleotideo = input(f'Digite o {len(lista) + 1}° nucleotídeo de {vezes}: ')
        lista.append(nucleotideo)

    if vezes != 0:
        print(f"Sequência de DNA: {''.join(lista).translate(mapeamento)}")
    else:
        print('Programa finalizado.')


print('Sequenciador de DNA')
print('Nucleotídeos A, C, G e T correspondem respectivamente a 1, 2, 3 e 4.')
sequencia_dna()
