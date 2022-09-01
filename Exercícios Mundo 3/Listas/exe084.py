'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

from traceback import print_last


pessoas = list()
dados = list()
mai = men = 0

while True:
    dados.append(input('Nome: ').strip().capitalize())
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    while True:
        option = input('Quer continuar? [S/N] ').strip().upper()
        if option == 'S' or option == 'N':
            break
    if option == 'N':
        break


print(f'Pessoas cadastradas: {len(pessoas)}')
print(f'O maior peso resgistrado: {mai}Kg. Peso de: ',end='')
for p in pessoas:
    if p[1] == mai:
        print(f'{p[0]}',end=' ')
print(f'\nO mensor peso registrado: {men}Kg. Peso de: ',end='')
for p in pessoas:
    if p[1] == men:
        print(f'[{p[0]}] ',end=' ')