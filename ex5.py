
sexo = input('Digite o sexo da pessoa (M/F): ')
sexo = sexo.lower()

def comeco(sexof):
    sexof = input('Digite o sexo da pessoa (M/F): ')
    sexof = sexof.lower()
    return sexo

while sexo != 'm' and sexo != 'f':
    print('ERRO! Digite apenas M ou F.')
    sexo = comeco(sexo)



idade = int(input('Digite a idade da pessoa: '))
trabalho = int(input('Digite quantos anos a pessoa trabalhou: '))

match sexo:
    case 'm':
        if idade >= 65 and trabalho >= 10:
            print('Aposentavel')
        elif idade >= 63 and idade < 65 and trabalho >= 15:
            print('Aposentavel')
        else:
            print('Nao Aposentavel')
    case 'f':
        if idade >= 63 and trabalho >= 10:
            print('Aposentavel')
        elif idade >= 61 and idade < 63 and trabalho >= 15:
            print('Aposentavel')
        else:
            print('Nao Aposentavel')
