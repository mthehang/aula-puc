import os

traducao = str.maketrans({'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A'})  # meu dicionário para parear a cadeia
dna: list = []  # declarando que DNA é uma lista vazia


def menu():
    print('1 - Inserir uma cadeia de bases nitrogenadas')
    print('2 - Contar bases nitrogenadas da cadeia')
    print('3 - Inserir bases nitrogenadas na cadeia criada')
    print('4 - Parear cadeia criada')
    print('5 - Contar uma subcadeia de bases nitrogenadas')
    print('6 - Inverter cadeia criada')
    print('7 - Verificar problemas de pareamento')
    print('8 - Cortar cadeia')
    print('9 - Resetar DNA')
    print('0 - Sair do programa')


def verificar_fita2():
    if len(dna) > 1:
        while True:
            if len(dna[0]) == len(dna[1]):
                print(f'Fita 1: {dna[0]} ')
                print(f'Fita 2 detectada: {dna[1]} ')
                resposta = input('Deseja usá-la? (S/N)\n').lower()
                if resposta == 's':
                    return
                elif resposta == 'n':
                    del dna[1]
                    break
                else:
                    print('Resposta inválida.')
            else:
                print('A Fita 2 é menor que a Fita 1.')
                print('É necessário parear fitas.')
                return 1


def resetar_dna():
    dna.clear()


def cortar_cadeia():
    print(f'Fita 1: {dna[0]}')
    print(f'Fita 2: {dna[1]}')
    corte = input('Digite o que deseja cortar da Fita 1: ').upper()

    achar = [i for i in range(len(dna[0])) if dna[0].startswith(corte, i)]

    if not achar:
        print(f'"{corte}" não foi encontrado na cadeia.')
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
                elif resp == '2':
                    dna[0] = dna[0][:index_atual] + dna[0][index_atual + len(corte):]
                    dna[1] = dna[1][:index_atual] + dna[1][index_atual + len(corte):]
                    if dna[0]:
                        print(f'Fita 1 atualizada: {dna[0]}')
                        print(f'Fita 2 atualizada: {dna[1]}')
                        break
                    else:
                        resetar_dna()
                        print('DNA resetado,')
                        break
                else:
                    print('Resposta inválida.')
            break
        elif resposta.upper() == 'P':
            index = (index + 1) % len(
                achar)  # Iterar todos os index, pois quando index+1 % len acontecer, retornará 0, resetando
        elif resposta.upper() == 'N':
            print('Operação cancelada.')
            break
        else:
            print('Resposta inválida. Tente novamente.')


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
            print(f'Cadeia: {dna[0]}')
            print(f'Subcadeia: {subcadeia}')
            print(f'Quantidade de subcadeias encontradas: {quantidade}')
            break
        else:
            print('\nBase nitrogenada inválida!\n')


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


def contar_bases():
    while True:
        base_nitrogenada = input('Digite a base nitrogenada (A, C, T, G) que deseja contar: ').upper()
        if base_nitrogenada in ['A', 'C', 'T', 'G']:
            break
        else:
            print("Valor inválido. Por favor, insira apenas (A, C, G, T).")
    print(f'\nFita 1: {dna[0]}')
    print(f'Quantidade de "{base_nitrogenada}" na fita 1: {dna[0].count(base_nitrogenada)}')


def inserir_bases():
    while True:
        resposta = input(f'Insira sua bases nitrogenadas (A, C, G, T) na cadeia {dna[0]}: ').upper()
        if resposta and all(char in ['A', 'C', 'G', 'T'] for char in resposta):
            dna[0] += resposta
            print(f'\nCadeia atualizada: {dna[0]}')
            break
        else:
            print('\nBase nitrogenada inválida!\n')


def verificar_pareamento():
    while True:
        if verificar_fita2() == 1:
            return
        else:
            os.system('cls')
            while True:
                print(f'Fita 1: {dna[0]}')
                dna.append(input('Digite a cadeia que deseja verificar pareamento: ').upper())
                if len(dna[1]) != len(dna[0]):
                    print('A cadeia inserida não tem o mesmo tamanho que a cadeia da Fita 1.')
                    del dna[1]
                else:
                    if all(char in ['A', 'C', 'G', 'T'] for char in dna[1]):
                        pareamentos_errados = []
                        for i in range(len(dna[0])):
                            if dna[1].translate(traducao)[i] != dna[0][i]:
                                pareamentos_errados.append(f'{i + 1}')
                        if not pareamentos_errados:
                            os.system('cls')
                            print(f'Fita 1: {dna[0]}')
                            print(f'Fita 2: {dna[1]}')
                            print('Cadeia perfeitamente pareada.')
                            break
                        else:
                            print(f'Erro de pareamento na(s) posição(ões): {", ".join(pareamentos_errados)}')
                            print('Fita 2 criada será deletada.')
                            del dna[1]
                            break
                    else:
                        print("Valor inválido. Por favor, insira apenas (A, C, G, T).")


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
