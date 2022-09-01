#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

numeros = list()
for c in range (0,5):
    numeros.append(int(input(f'Digite um valor para posição {c}: ')))
print(f'Valores digitados: {numeros}')
print('='*40)
print(f'O maior valor digitado foi: {max(numeros)} nas posições: ',end='')
for i, n in enumerate(numeros):
    if n == max(numeros):
        print(f'{i}...',end='')
print(f'\nO menor valor digitado foi: {min(numeros)} e se encontra nas posições: ',end='')
for i, n in enumerate(numeros):
    if n == min(numeros):
        print(f'{i}... ',end='')