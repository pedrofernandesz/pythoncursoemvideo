#Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

v = input('Digite um nome: ')
print(f'O tipo primitivo deste valor é {type(v)}')
print(f'Só tem espaços? {v.isspace()}')
print(f'É um número? {v.isnumeric()}')
print(f'É alfabético? {v.isalpha()}')
print(f'É alfanumérico? {v.isalnum()}')
