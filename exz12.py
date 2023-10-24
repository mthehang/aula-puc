
lista = [4, 5, 2, 3]

for items in range(len(lista)):
    while items < 2:
        lista[items] = 7
        items += 1
    print(lista)

lista.append(9)

print(lista[-1])

lista = [8, 8, 8, 8]

print(lista)
