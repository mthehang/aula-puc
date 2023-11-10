import os

traducao = str.maketrans({'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A'})  # meu dicionário para parear a cadeia
dna: list = []  # declarando que DNA é uma lista vazia


def menu():
    print('1 - Inserir uma cadeia de bases nitrogenadas na Fita 1 do DNA')
    print('2 - Contar e Localizar bases nitrogenadas da cadeia')
    print('3 - Inserir bases nitrogenadas na cadeia criada')
    print('4 - Parear cadeia criada')
    print('5 - Contar uma subcadeia de bases nitrogenadas')
    print('6 - Inverter cadeia criada')
    print('7 - Verificar problemas de pareamento')
    print('8 - Cortar cadeia')
    print('9 - Resetar DNA')
    print('0 - Sair do programa')


def resetar_dna():
    dna.clear()


def cortar_cadeia():
    print(f'Fita 1: {dna[0]}')
    print(f'Fita 2: {dna[1]}')
    corte = input('Digite o que deseja cortar da Fita 1: ').upper()

    achar = [i for i in range(len(dna[0])) if dna[0].startswith(corte, i)]

    if not achar:
        os.system('cls')
        print(f'"{corte}" não foi encontrado na cadeia {dna[0]}.')
        return

    index = 0
    while True:
        index_atual = achar[index]
        grifado1 = dna[0][:index_atual] + '-' + dna[0][index_atual:index_atual + len(corte)] + '-' + dna[0][
                                                                                                     index_atual + len(
                                                                                                         corte):]
        grifado2 = dna[1][:index_atual] + '-' + dna[1][index_atual:index_atual + len(corte)] + '-' + dna[1][
                                                                                                     index_atual + len(
                                                                                                         corte):]
        os.system('cls')
        print(f'Fita 1: {grifado1}')
        print(f'Fita 2: {grifado2}')
        resposta = input('Deseja cortar aqui (S/N)' + (
            ' ou cortar próxima subcadeia igual (P)? ' if len(achar) > 1 else '? ')).upper()
        if resposta == 'S':
            while True:
                print('1 - Substituir subcadeia')
                print('2 - Remover subcadeia')
                resp = input('Digite o que deseja: ')
                if resp == '1':
                    while True:
                        novasub = input('Digite a nova subcadeia: ').upper()
                        if novasub and all(char in ['A', 'C', 'G', 'T'] for char in novasub):
                            dna[0] = dna[0][:index_atual] + novasub + dna[0][index_atual + len(corte):]
                            dna[1] = dna[1][:index_atual] + novasub.translate(traducao) + dna[1][
                                                                                          index_atual + len(corte):]
                            print(f'Fita 1 atualizada: {dna[0]}')
                            print(f'Fita 2 atualizada: {dna[1]}')
                            return
                        else:
                            print('Subcadeia inválida.')
                            input('Pressione ENTER para tentar novamente')
                            os.system('cls')
                elif resp == '2':
                    dna[0] = dna[0][:index_atual] + dna[0][index_atual + len(corte):]
                    dna[1] = dna[1][:index_atual] + dna[1][index_atual + len(corte):]
                    if dna[0]:
                        print(f'Fita 1 atualizada: {dna[0]}')
                        print(f'Fita 2 atualizada: {dna[1]}')
                        break
                    else:
                        resetar_dna()
                        os.system('cls')
                        print('DNA resetado.')
                        break
                else:
                    print('Resposta inválida.')
                    input('Pressione ENTER para tentar novamente.')
                    os.system('cls')
            break
        elif resposta.upper() == 'P':
            index = (index + 1) % len(
                achar)  # Iterar todos os index, pois quando index+1 % len acontecer, retornará 0, resetando
        elif resposta.upper() == 'N':
            print('Operação cancelada.')
            break
        else:
            print('Resposta inválida.')
            input('Pressione ENTER para tentar novamente.')
            os.system('cls')


def inverter():
    print(f'Cadeia: {dna[0]}')
    print(f'Cadeia invertida: {dna[0][::-1]}')


def localizar_subcadeia():
    while True:
        print(f'Cadeia: {dna[0]}')
        subcadeia = input('Digite a subcadeia que deseja contar: ').upper()
        if subcadeia and all(char in ['A', 'C', 'G', 'T'] for char in subcadeia):  # subcadeia para nao ser nula e
            # all retorna true se todas condições forem
            # atendidas, retorna false se não
            quantidade = sum(
                1 for i in range(len(dna[0]) - len(subcadeia) + 1) if dna[0][i:i + len(subcadeia)] == subcadeia)
            # range(len(cadeia) - len(subcadeia) + 1) pode "deslizar" do índice 0 ao tamanho da cadeia - subcadeia,
            # para nao passar do tamanho da cadeia
            # for i in range() é para iterar
            os.system('cls')
            print(f'Cadeia: {dna[0]}')
            print(f'Subcadeia: {subcadeia}')
            print(f'Quantidade de subcadeias encontradas: {quantidade}')
            break
        else:
            print('\nBase nitrogenada inválida!\n')
            input('Pressione ENTER para tentar novamente.')
            os.system('cls')


def parear():
    if len(dna) < 2:
        dna.append(dna[0].translate(traducao))
    else:
        dna[1] = dna[0].translate(traducao)
    print(f'Fita 1 do DNA: {dna[0]}')
    print(f'Fita pareada do DNA: {dna[1]}')


def inserir_fitas():
    while True:
        resposta = input('Digite sua cadeia (A, C, G, T) para a fita do DNA, sem espaços: ').upper()
        if resposta and all(char in ['A', 'C', 'G', 'T'] for char in resposta):
            dna.append(resposta)
            print(f'\nFita 1: {dna[0]}')
            break
        else:
            print('\nBase nitrogenada inválida!\n')
            input('Pressione ENTER para tentar novamente.')
            os.system('cls')


def localizar_bases(base):
    posicoes = [str(i+1) for i, char in enumerate(dna[0]) if char == base]
    print(f'Posições encontradas: {", ".join(posicoes)}')


def contar_bases():
    while True:
        base_nitrogenada = input('Digite a base nitrogenada (A, C, T, G) que deseja contar e localizar: ').upper()
        if base_nitrogenada in ['A', 'C', 'T', 'G']:
            if base_nitrogenada in dna[0]:
                break
            else:
                os.system('cls')
                print(f'Fita 1: {dna[0]}')
                print(f'Base nitronegada "{base_nitrogenada}" não foi encontrada.')
                return
        else:
            print("Valor inválido. Por favor, insira apenas (A, C, G, T).")
            input('Pressione ENTER para tentar novamente.')
            os.system('cls')
    print(f'\nFita 1: {dna[0]}')
    print(f'Quantidade de "{base_nitrogenada}" na fita 1: {dna[0].count(base_nitrogenada)}')
    localizar_bases(base_nitrogenada)


def inserir_bases():
    while True:
        resposta = input(f'Insira sua bases nitrogenadas (A, C, G, T) na cadeia {dna[0]}: ').upper()
        if resposta and all(char in ['A', 'C', 'G', 'T'] for char in resposta):
            dna[0] += resposta
            print(f'\nCadeia atualizada: {dna[0]}')
            break
        elif not resposta:
            print('\nOperação cancelada.')
            break
        else:
            print('\nBase nitrogenada inválida!\n')
            input('Pressione ENTER para tentar novamente.')
            os.system('cls')


def criando_pareamento():
    while True:
        print(f'Fita 1: {dna[0]}')
        fita2 = input('Digite a cadeia da Fita 2: ').upper()
        if fita2 and len(fita2) != len(dna[0]):
            print('A cadeia inserida não tem o mesmo tamanho que a cadeia da Fita 1.')
        elif fita2 and all(char in ['A', 'C', 'G', 'T'] for char in fita2):
            dna.append(fita2)
            break
        elif not fita2:
            print('Operação cancelada')
            return 1
        else:
            print("Valor inválido. Por favor, insira apenas (A, C, G, T).")
            input('Pressione ENTER para tentar novamente.')
            os.system('cls')


def verificar_pareamento():
    if len(dna) < 2:
        if criando_pareamento() == 1:
            return

    elif len(dna[0]) != len(dna[1]):
        print(f'Fita 1: {dna[0]}')
        print(f'Fita 2: {dna[1]}')
        print('As fitas de DNA têm tamanhos diferentes. É necessário parear (Opção 4).')
        return

    else:
        while True:
            print(f'Fita 1: {dna[0]}')
            print(f'Fita 2: {dna[1]}')
            resposta = input('Deseja usar esta Fita 2? (S/N)\n').lower()
            if resposta == 'n':
                dna.pop()
                criando_pareamento()
                os.system('cls')
                break
            elif resposta == 's':
                os.system('cls')
                break
            else:
                print('Resposta inválida.')
                input('Pressione ENTER para tentar novamente.')
                os.system('cls')
    pareamentos_errados = [str(i + 1) for i in range(len(dna[0])) if dna[1][i] != dna[0][i].translate(traducao)]
    if not pareamentos_errados:
        print(f'Fita 1: {dna[0]}')
        print(f'Fita 2: {dna[1]}')
        print('As fitas estão corretamente pareadas.')
    else:
        print(f'Erro de pareamento na(s) posição(ões): {", ".join(pareamentos_errados)}')
        print('Fita com defeito está sendo deletada.')
        dna.pop()


def main():
    global dna
    while True:
        os.system('cls')
        menu()
        try:
            opcao = int(input('Digite o que deseja: '))
            match opcao:
                case 1:
                    os.system('cls')
                    resetar_dna()
                    inserir_fitas()
                    input('\nPressione enter para continuar.')
                case 2:
                    os.system('cls')
                    if dna:
                        contar_bases()
                    else:
                        print('\nDNA vazio.')
                    input('\nPressione enter para continuar.')
                case 3:
                    os.system('cls')
                    if dna:
                        inserir_bases()
                    else:
                        print('DNA vazio.')
                    input('\nPressione enter para continuar.')
                case 4:
                    os.system('cls')
                    if dna:
                        parear()
                    else:
                        print('DNA vazio.')
                    input('\nPressione enter para continuar.')
                case 5:
                    os.system('cls')
                    if dna:
                        localizar_subcadeia()
                    else:
                        print('DNA vazio.')
                    input('\nPressione enter para continuar.')
                case 6:
                    os.system('cls')
                    if dna:
                        inverter()
                    else:
                        print('DNA vazio.')
                    input('\nPressione enter para continuar.')
                case 7:
                    os.system('cls')
                    if dna:
                        verificar_pareamento()
                    else:
                        print('DNA vazio')
                    input('\nPressione enter para continuar.')
                case 8:
                    os.system('cls')
                    if len(dna) > 1:
                        if len(dna[0]) == len(dna[1]):
                            cortar_cadeia()
                        else:
                            print('Fitas com tamanhos diferentes, verifique pareamento.')
                    else:
                        print('DNA incompleto.')
                    input('\nPressione enter para continuar.')
                case 9:
                    os.system('cls')
                    if dna:
                        resetar_dna()
                        print('DNA resetado com sucesso.')
                    else:
                        print('DNA vazio')
                    input('\nPressione enter para continuar.')
                case 0:
                    os.system('cls')
                    print('\nFinalizando o programa.')
                    exit()
                case __:
                    os.system('cls')
                    print('\nOpção inválida.')
                    input('\nPressione enter para continuar.')
        except ValueError:
            os.system('cls')
            print('\nOpção inválida.')
            input('\nPressione enter para continuar.')


main()
