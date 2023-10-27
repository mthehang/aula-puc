lista = []
while len(lista) < 10:
    lista.append(int(input(f'Digite o {len(lista) + 1}º número: ')))

print(lista)
lista.sort(reverse=True)
print(lista)
