
idade = int(input('Digite sua idade: '))
cursando = input('Você está cursando graduação? S/N ')
cursando = cursando.lower()

if idade < 21:
    print('É dependente no IR')
elif idade > 21 and idade <= 24 and cursando == 's':
    print('É dependente no IR')
elif idade > 24:
    print('Não é dependente no IR')