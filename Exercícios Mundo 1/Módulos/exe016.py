# Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.


from math import trunc
number = float(input('Digite um número: '))
print(f'O número {number} tem sua parte inteira: {trunc(number)}')