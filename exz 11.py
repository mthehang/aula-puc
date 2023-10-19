lista = []
while len(lista) < 10:
    lista.append(int(input(f'Digite o {len(lista) + 1}º número: ')))

flag = 9

while flag >= 0:
    print(lista[flag])
    flag -= 1
