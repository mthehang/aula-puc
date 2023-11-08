import os


def write(something):
    with open("C:/Users/mathe/Documents/Programacao PUC/things.txt", "a") as f:
        f.write(f'{something}\n')


def read():
    with open("C:/Users/mathe/Documents/Programacao PUC/things.txt", "r") as f:
        return [line.strip().split(';') for line in f]


def alterar_contato():
    contatos = read()
    try:
        indice = int(input('Digite o índice do contato que deseja alterar: '))
        if 1 <= indice <= len(contatos):
            print(f'Alterando contato: Nome: {contatos[indice - 1][0]} - Telefone: {contatos[indice - 1][1]}')
            novo_nome = input('Digite o novo nome: ').capitalize()
            novo_numero = input('Digite o novo número de telefone: ')
            contatos[indice - 1] = [novo_nome, novo_numero]
            with open("C:/Users/mathe/Documents/Programacao PUC/things.txt", "w") as f:
                for contato in contatos:
                    f.write(';'.join(contato) + '\n')
            print("Contato alterado com sucesso!")
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
    print('b - Inserir contato')
    print('c - Ver contato específico')
    print('d - Alterar contato')
    print('z - Sair do programa')


def continuar_sair():
    print()
    print('x - Voltar ao menu')
    print('z - Sair do programa')
    while True:
        op = input('Digite o que deseja: ').lower()
        match op:
            case 'x':
                break
            case 'z':
                exit()
            case _:
                print('Opção inválida.')


def main():
    while True:
        os.system('cls')
        menu()
        opcao = input('Digite o que deseja: ').lower()
        match opcao:
            case 'a':
                os.system('cls')
                contatos = read()
                for index, lista in enumerate(contatos, start=1):
                    print(f'{index} - Nome: {lista[0]} - Telefone: {lista[1]}')
                    print()
                continuar_sair()
            case 'b':
                os.system('cls')
                nome = input('Digite o nome: ').capitalize()
                numero = input('Digite o número de telefone: ')
                contatos = read()
                if [nome, numero] not in contatos:
                    write(nome + ';' + numero)
                else:
                    print("Contato já existe.")
                continuar_sair()
            case 'c':
                os.system('cls')
                procurar()
                continuar_sair()
            case 'd':
                os.system('cls')
                alterar_contato()
                continuar_sair()
            case 'z':
                exit()
            case _:
                print('Opção inválida.')
                input()


main()
