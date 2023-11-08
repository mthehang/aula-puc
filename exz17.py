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


tabela = ['X', 'X', 'O',
          'O', 'O', 'X',
          'X', 'O', 'O']

vencedor = verificar_vencedor(tabela)
if vencedor:
    print(f"{vencedor} ganhou!")
else:
    print("Ninguém ganhou.")
