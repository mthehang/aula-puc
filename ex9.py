
numero = int(input('Digite um numero: '))

if not numero < 8 and not numero > 256 or not numero < 300 and not numero > 512:
    print('O numero esta entre os intervalos definidos.')
else:
    print('O numero nao esta nos intervalos')