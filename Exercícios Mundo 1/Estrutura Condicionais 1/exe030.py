#Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

number = int(input('Digite um número inteiro: '))
if number % 2 == 0:
    print(f'{number} é par')
else:
    print(f'{number} é ímpar')