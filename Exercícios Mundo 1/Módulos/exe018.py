#Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

number = float(input('Digite o ângulo: '))
print(f'Seno: {math.sin(math.radians(number))}')
print(f'Cosseno: {math.cos(math.radians(number))}')
print(f'Tangente: {math.tan(math.radians(number))}')