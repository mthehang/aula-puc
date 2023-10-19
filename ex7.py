
numero = int(input('Digite um numero: '))

if numero >= 8 and numero <= 256:
    print(f'O numero {numero} esta no intervalo [8, 256]')
else:
    print(f'O numero {numero} nao esta no intervalo [8, 256]')