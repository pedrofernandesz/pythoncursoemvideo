#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

tupla = (randint(0,10), randint(0,10), randint(0,10),
        randint(0,10))
print('Números sorteados: ',end='')
for c in tupla:
    print(c, end=' ')
print(f'\nMaior valor: {max(tupla)}')
print(f'Menor valor: {min(tupla)}')