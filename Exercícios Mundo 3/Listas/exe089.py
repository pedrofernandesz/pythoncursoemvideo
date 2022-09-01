#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

alunos = list()
dado = list()
while True:
    name = input('Nome: ').strip().capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2)/2
    alunos.append([name,[nota1, nota2], media])
    while True:
        option = input('Quer continuar? [S/N] ').strip().upper()
        if option == 'S' or option == 'N':
            break
    if option == 'N':
        break

print('-='*30)
print(f'{"c":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for i, aluno in enumerate(alunos):
    print(f'{i:<4} {aluno[0]:<10} {aluno[2]:>8.1f}')
while True:
    option = int(input('Mostrar nota de qual aluno? (999 para finalizar )'))
    if option == 999:
        break
    if option <= len(alunos) - 1:
        print(f'Notas de {alunos[option][0]} são {alunos[option][1]} ')