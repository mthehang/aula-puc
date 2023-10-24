
def loop():
    for items in lista:
        print(items.capitalize())

lista = ['matheus','leticia', 'valeria']
loop()
print()
lista[1:2] = ['safira']
loop()
lista
print(f'\nQuantidade de itens na lista: {len(lista)}')

lista.remove('safira')
loop()
