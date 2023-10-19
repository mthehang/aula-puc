
numero = int(input('Digite um número: '))

if not numero < 8 and not numero > 256 or not numero < 300 and not numero > 512:
    print('O número está entre os intervalos definidos.')
else:
    print('O número não está nos intervalo')