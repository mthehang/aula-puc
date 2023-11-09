import os


def verificar_arquivo():
    arquivo = "things.txt"
    if not os.path.isfile(arquivo):
        open(arquivo, 'w').close()


def write(something):
    with open("things.txt", "a") as f:
        f.write(f'{something}\n')


def read():
    with open("things.txt", "r") as f:
        return [line.strip().split(';') for line in f]


def procurar_contato():
    contatos = read()
    pesquisa = input('Digite o nome ou telefone do contato para procurá-lo: ').capitalize()
    contatos_encontrados = [contato for contato in contatos if pesquisa in contato[0] or pesquisa in contato[1]]
    if contatos_encontrados:
        for contato in contatos_encontrados:
            print(f'Nome: {contato[0]} - Telefone: {contato[1]}')
    else:
        print('Nenhum contato encontrado.')


def resetar():
    while True:
        resp = input('Você tem certeza? (S/N)\n').lower()
        if resp not in ['s', 'n']:
            print('Opção inválida.')
        else:
            break
    if resp == 's':
        with open("things.txt", "w") as f:
            f.write("")
    else:
        print('Operação cancelada.')


def remover_contato():
    contatos = read()
    pesquisa = input('Digite o nome ou telefone do contato para removê-lo: ').capitalize()
    contatos_encontrados = [contato for contato in contatos if pesquisa in contato[0] or pesquisa in contato[1]]
    if contatos_encontrados:
        for i, contato in enumerate(contatos_encontrados):
            print(f'{i+1} - Nome: {contato[0]} - Telefone: {contato[1]}')
        indice = int(input('Digite o número do contato que deseja remover: ')) - 1
        if 0 <= indice < len(contatos_encontrados):
            while True:
                resp = input('Você tem certeza? (S/N)\n').lower()
                if resp not in ['s', 'n']:
                    print('Opção inválida.')
                else:
                    break
            if resp == 's':
                contatos.remove(contatos_encontrados[indice])
                with open("things.txt", "w") as f:
                    for contato in contatos:
                        f.write(';'.join(contato) + '\n')
                print("Contato removido com sucesso!")
            else:
                print('Operação cancelada.')
        else:
            print('Índice fora do intervalo.')
    else:
        print('Nenhum contato encontrado.')


def remover_indice():
    contatos = read()
    try:
        indice = int(input('Digite o índice do contato que deseja remover: '))
        if 1 <= indice <= len(contatos):
            print(f'Removendo contato: Nome: {contatos[indice - 1][0]} - Telefone: {contatos[indice - 1][1]}')
            while True:
                resp = input('Você tem certeza? (S/N)\n').lower()
                if resp not in ['s', 'n']:
                    print('Opção inválida.')
                else:
                    break
            if resp == 's':
                del contatos[indice - 1]
                with open("things.txt", "w") as f:
                    for contato in contatos:
                        f.write(';'.join(contato) + '\n')
                print("Contato removido com sucesso!")
            else:
                print('Operação cancelada.')
        else:
            print("Índice fora do intervalo da lista de contatos.")
    except ValueError:
        print("Por favor, digite um número inteiro.")


def alterar_contato():
    contatos = read()
    try:
        indice = int(input('Digite o índice do contato que deseja alterar: '))
        if 1 <= indice <= len(contatos):
            print(f'Alterando contato: Nome: {contatos[indice - 1][0]} - Telefone: {contatos[indice - 1][1]}')
            while True:
                resp = input('Você tem certeza? (S/N)\n').lower()
                if resp not in ['s', 'n']:
                    print('Opção inválida.')
                else:
                    break
            if resp == 's':
                novo_nome = input('Digite o novo nome: ').capitalize()
                novo_numero = input('Digite o novo número de telefone: ')
                contatos[indice - 1] = [novo_nome, novo_numero]
                with open("things.txt", "w") as f:
                    for contato in contatos:
                        f.write(';'.join(contato) + '\n')
                print("Contato alterado com sucesso!")
            else:
                print('Operação cancelada.')
        else:
            print("Índice fora do intervalo da lista de contatos.")
    except ValueError:
        print("Por favor, digite um número inteiro.")


def procurar():
    contatos = read()
    try:
        indice = int(input('Digite o índice do contato que deseja ver: '))
        if 1 <= indice <= len(contatos):
            contato_especifico = contatos[indice - 1]  # Ajuste para índice base-0
            print(f'Nome: {contato_especifico[0]} - Telefone: {contato_especifico[1]}')
            return contato_especifico
        else:
            print("Índice fora do intervalo da lista de contatos.")
    except ValueError:
        print("Por favor, digite um número inteiro.")


def menu():
    print('a - Listar agenda')
    print('b - Cadastrar contato')
    print('c - Procurar contato pelo índice')
    print('d - Procurar contato por nome ou telefone')
    print('e - Alterar contato pelo índice')
    print('f - Remover contato pelo índice')
    print('g - Remover contato pelo nome ou telefone')
    print('h - Resetar a agenda')
    print('z - Sair do programa')


def main():
    while True:
        os.system('cls')
        menu()
        opcao = input('Digite o que deseja: ').lower()
        match opcao:
            case 'a':
                verificar_arquivo()
                os.system('cls')
                contatos = read()
                if len(contatos) > 0:
                    for index, lista in enumerate(contatos, start=1):
                        print(f'{index} - Nome: {lista[0]} - Telefone: {lista[1]}')
                        print()
                else:
                    print('A agenda está vazia.')
                input()
            case 'b':
                verificar_arquivo()
                os.system('cls')
                print('Cadastrar contato')
                nome = input('Digite o nome: ').capitalize()
                numero = input('Digite o número de telefone: ')
                contatos = read()
                numero_existe = any(contato[1] == numero for contato in contatos)
                if not numero_existe:
                    write(nome + ';' + numero)
                    print('Contato cadastrado com sucesso!')
                else:
                    print("Número de telefone já cadastrado.")
                input()
            case 'c':
                verificar_arquivo()
                os.system('cls')
                procurar()
                input()
            case 'd':
                verificar_arquivo()
                os.system('cls')
                procurar_contato()
                input()
            case 'e':
                verificar_arquivo()
                os.system('cls')
                alterar_contato()
                input()
            case 'f':
                verificar_arquivo()
                os.system('cls')
                remover_indice()
                input()
            case 'g':
                verificar_arquivo()
                os.system('cls')
                remover_contato()
                input()
            case 'h':
                verificar_arquivo()
                resetar()
                input()
            case 'z':
                exit()
            case _:
                print('Opção inválida.')
                input()

main()
