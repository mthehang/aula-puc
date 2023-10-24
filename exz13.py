
lista = []

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
    print(items)
