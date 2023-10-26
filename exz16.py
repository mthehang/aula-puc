
while True:
    try:
        vezes = int(input('Digite quantos números você quer digitar: '))
        if vezes == 0:
            print('Programa finalizado.')
        break
    except ValueError:
        print('Digite um número válido.')
        
while True:
    try:
        lista = []
        while len(lista) < vezes:
            lista.append(int(input('Digite um número: ')))
        break
    except ValueError:
        print('Digite um número válido.')
        
lista_pares = []
lista_indice_pares = []

for items in lista:
    if items % 2 == 0: # índice pares
        lista_pares.append(items)
        
for indice in range(len(lista)):
    if indice % 2 == 0:
        lista_indice_pares.append(lista[indice])
        
        
print(f'Números pares da lista: {lista_pares}')
print(f'Números de índices pares da lista: {lista_indice_pares}')

