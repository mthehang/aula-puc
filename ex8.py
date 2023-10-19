
numero = int(input('Digite um numero: '))

if numero >= 8 and numero <= 256:
    print(f'O numero {numero} esta no intervalo [8, 256]')
elif numero >= 300 and numero <= 512:
    print(f'O numero {numero} esta no intervalo [300, 512]')
else:
    print(f'O numero {numero} nao esta nem no intervalo [8, 256] e nem em [300, 512]')