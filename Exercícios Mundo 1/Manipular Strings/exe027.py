# Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

name = input('Nome completo: ').strip().capitalize().split()
print(f'Primeiro nome: {name[0]}')
print(f'Último nome: {name[-1]}')