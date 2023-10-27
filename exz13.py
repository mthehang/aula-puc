lista = []


def write(something):
    f = open("C:/Users/mathe/Documents/Programacao PUC/things.txt", "a")
    f.writelines(f'{something}\n')
    f.close()


def read():
    f = open("C:/Users/mathe/Documents/Programacao PUC/things.txt", "r")
    name = f.readlines()
    f.close()
    return name


def funcao():
    while True:
        try:
            vezes = int(input('Quantos nomes deseja escrever? '))
            break
        except ValueError:
            print('Digite um número válido.')

    while len(lista) < vezes:
        contador = vezes - len(lista)
        if contador > 1:
            while True:
                nome = input(f'Digite {contador} nomes: ').capitalize()
                if nome != '' and not any(char.isdigit() for char in nome):
                    lista.append(nome)
                    break
                else:
                    print('Digite um nome válido.')

        else:
            while True:
                nome = input(f'Digite {contador} nome: ').capitalize()
                if nome != '' and not any(char.isdigit() for char in nome):
                    lista.append(nome)
                    break
                else:
                    print('Digite um nome válido.')

    for items in lista:
        write(items)

    print(f'Você já salvou {len(read())} nomes:')

    for items in read():
        print(items)


funcao()
