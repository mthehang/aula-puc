def menu():
    while True:  # Loop para o nome
        nome = input('Digite o nome: ').capitalize()
        if nome != '' and not any(char.isdigit() for char in nome):
            break
        else:
            print('Nome inválido!')

    while True:  # Loop para o sexo
        sexo = input('Digite o sexo (M/F): ').lower()
        if sexo in ['m', 'f']:
            break
        else:
            print('Por favor, digite M para masculino ou F para feminino.')

    while True:  # Loop para a massa
        try:
            massa = float(input('Digite a massa corporal (KG): ').replace(',', '.'))
            if massa != 0:
                break
            else:
                print('A massa não pode ser 0. Tente novamente.')
        except ValueError:
            print('Por favor, digite um valor válido para a massa.')

    while True:  # Loop para a altura
        try:
            altura = float(input('Digite a altura (metros): ').replace(',', '.'))
            if altura != 0:
                break
            else:
                print('A altura não pode ser 0. Tente novamente.')
        except ValueError:
            print('Por favor, digite um valor válido para a altura.')

    imc = massa / (altura ** 2)

    match sexo:  # Switch
        case 'm':
            if imc < 20:
                print(f'IMC de {nome} está abaixo do normal.')
            elif 20 <= imc < 25:
                print(f'IMC de {nome} está normal.')
            elif 25 <= imc < 30:
                print(f'IMC de {nome} está em obesidade Leve.')
            elif 30 <= imc < 40:
                print(f'IMC de {nome} está em obesidade Moderada.')
            else:
                print(f'IMC de {nome} está em obesidade Mórbida.')
        case 'f':
            if imc < 19:
                print(f'IMC de {nome} está abaixo do normal.')
            elif 19 <= imc < 24:
                print(f'IMC de {nome} está normal.')
            elif 24 <= imc < 29:
                print(f'IMC de {nome} está em obesidade Leve.')
            elif 29 <= imc < 39:
                print(f'IMC de {nome} está em obesidade Moderada.')
            else:
                print(f'IMC de {nome} está em obesidade Mórbida.')


print('Calculadora de IMC.')
menu()
