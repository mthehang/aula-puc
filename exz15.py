import random

lista = []

while True:
    try:
        quantidade = int(input('Digite a quantidade de números aleatórios que deseja gerar: '))
        if quantidade == 0:
            print('Programa finalizado.')
        break
    except ValueError:
        print('Quantidade inválida.')

while len(lista) < quantidade:
    lista.append(random.randrange(1, 100))

for items in lista:
    print(items)
