
aluguel = float(input('Digite o valor do aluguel: '))
dia = int(input('Diga o dia do pagamento: '))

if dia >= 9 and dia <= 15:
    print(f'Voce precisa pagar R${aluguel}')
elif dia < 9:
    print(f'Voce precisa pagar R${aluguel*0.8}')
elif dia > 15:
    print(f'Voce precisa pagar R${aluguel + aluguel*0.2}')