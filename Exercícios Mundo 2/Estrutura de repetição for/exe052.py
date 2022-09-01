#Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

number = int(input('Digite um número: '))
cont = 0

for c in range(1, number + 1):
    if number % c == 0:
        print('\033[33m',end='')
        cont += 1
    else:
        print('\033[31m',end='')
    print(c,end=' ')

print(f'\n\033[mO número {number} é divisível por {cont} números')
if cont == 2:
    print('Por tanto é PRIMO')
else:
    print('Por tanto não é PRIMO')