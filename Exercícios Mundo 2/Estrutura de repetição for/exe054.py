#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

anoatual = date.today().year
maioridade = 0
menoridade = 0

for c in range(1, 8):
    birth = int(input(f'Em que a {c}° nasceu? '))
    if anoatual - birth < 18:
        menoridade += 1
    else:
        maioridade += 1
print(f'{maioridade} pessoas é maior de idade')
print(f'{menoridade} pessoas é menor de idade')