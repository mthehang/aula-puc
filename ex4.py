
nome = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a nota da primeira prova: '))
nota2 = float(input('Digite a nota da segunda prova: '))
media = (nota1 + nota2)/2
print(f'A media do(a) aluno(a) {nome} foi: {media}')
if media >= 9 and media <= 10:
    print('Aprovado com louvor!')
elif media >= 7.5 and media < 9:
    print('Aprovado com distincao.')
elif media >= 6 and media < 7.5:
    print('Aprovado.')
elif media >= 4 and media < 6:
    print('Exame.')
else:
    print('Reprovado!')