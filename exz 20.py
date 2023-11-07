alunos = 'Maria Eduarda;Luisa Schettini;Milena Coelho;Leticia Sayuri;Daniella Moreira;Carolina Matos'
print(alunos.upper())
print(alunos.lower())
lista = alunos.split(';')
print(lista)
print('Tente entender 1')
print(alunos.upper().split('LE'))
print('Tente entender 2')
print(alunos.upper().split('A'))
print('TENTE ENTENDER 3')
for i in range(len(lista)):
    print(lista[i].split()[::-1])
