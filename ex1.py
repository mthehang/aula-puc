
while True:
    try:
        valor = float(input('Digite o valor do produto R$'))
        if valor >= 0:
            break
        else:
            print('Valor inválido.')
            continue
    except ValueError:
        print('Valor inválido.')

parcelas = int(input(f'Em quantas vezes vai parcelar o valor de R${valor}? '))
print(f'O valor de cada parcela sera R${valor/parcelas}')