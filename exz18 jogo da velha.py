def verificar_vencedor(tabela):
    # Verificar linhas
    for i in range(0, 9, 3):
        if tabela[i] == tabela[i + 1] == tabela[i + 2] and tabela[i] != '0':
            return tabela[i]

    # Verificar colunas
    for i in range(3):
        if tabela[i] == tabela[i + 3] == tabela[i + 6] and tabela[i] != '0':
            return tabela[i]

    # Verificar diagonais
    if tabela[0] == tabela[4] == tabela[8] and tabela[0] != '0':
        return tabela[0]
    if tabela[2] == tabela[4] == tabela[6] and tabela[2] != '0':
        return tabela[2]

    return None  # Se ninguém ganhou


tabela = []
jogador1 = input('Digite a marcação do jogador 1: ')
jogador2 = input('Digite a marcação do jogador 2: ')
x = jogador1

while len(tabela) < 9:
    while True:
        try:
            jogada = int(input(f'Digite a posição da sua jogada {x} (0 a 8): '))
            if x == jogador1:
                x = jogador2
            else:
                x = jogador1
            break
        except ValueError:
            print('Jogada inválida.')

    tabela.insert(jogada, x)


vencedor = verificar_vencedor(tabela)
if vencedor:
    print(f"{vencedor} ganhou!")
else:
    print("Ninguém ganhou.")
