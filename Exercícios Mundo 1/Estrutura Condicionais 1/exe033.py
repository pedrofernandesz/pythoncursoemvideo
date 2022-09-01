# Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

number1 = int(input('Primeiro número: '))
number2 = int(input('Segundo número: '))
number3 = int(input('Terceiro número: '))

lista = [number1,number2,number3]
print(f'Maior número: {max(lista)}')
print(f'Menor número: {min(lista)}')