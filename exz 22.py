import os


def write(something):
    with open("things.txt", "a") as f:
        f.write(f'{something}\n')


def read():
    with open("things.txt", "r") as f:
        return [line.strip().split(';') for line in f]


def procurar_contato():
    contatos = read()
    pesquisa = input('Digite o início do nome ou parte do telefone do contato para procurá-lo: ')
    contatos_encontrados = [contato for contato in contatos if pesquisa in contato[0] or pesquisa in contato[1]]
    if contatos_encontrados:
        for contato in contatos_encontrados:
            print(f'Nome: {contato[0]} - Telefone: {contato[1]}')
    else:
        print('Nenhum contato encontrado.')


def resetar():
    resp = input('Você tem certeza disso? É irreversível! (S/N)').lower()
    while resp not in ['s', 'n']:
        print('Resposta inválida.')
    if resp == 's':
        with open("C:/Users/mathe/Documents/Programacao PUC/things.txt", "w") as f:
            f.write("")
    else:
        print('Operação cancelada.')


def remover_contato():
    contatos = read()
    try:
        indice = int(input('Digite o índice do contato que deseja remover: '))
        if 1 <= indice <= len(contatos):
            print(f'Removendo contato: Nome: {contatos[indice - 1][0]} - Telefone: {contatos[indice - 1][1]}')
            resp = input('Você tem certeza? (S/N)\n').lower()
            while resp not in ['s', 'n']:
                print('Opção inválida.')
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
            resp = input('Você tem certeza? (S/N)\n').lower()
            while resp not in ['s', 'n']:
                print('Opção inválida.')
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
    print('e - Alterar contato')
    print('f - Remover contato')
    print('g - Resetar a agenda')
    print('z - Sair do programa')


def main():
    while True:
        os.system('cls')
        menu()
        opcao = input('Digite o que deseja: ').lower()
        match opcao:
            case 'a':
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
                os.system('cls')
                procurar()
                input()
            case 'd':
                os.system('cls')
                procurar_contato()
                input()
            case 'e':
                os.system('cls')
                alterar_contato()
                input()
            case 'f':
                os.system('cls')
                remover_contato()
                input()
            case 'g':
                resetar()
                input()
            case 'z':
                exit()
            case _:
                print('Opção inválida.')
                input()


main()
