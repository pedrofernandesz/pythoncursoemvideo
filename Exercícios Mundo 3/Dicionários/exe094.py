'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

pessoas = list()
dados = dict()
s = 0

while True:
    dados['nome'] = input('Nome: ').strip().capitalize()
    while True:
        dados['sexo'] = input('Sexo: [M/F] ').strip().upper()
        if dados['sexo'] == 'M' or dados['sexo'] == 'F':
            break
    dados['idade'] = int(input('Idade: '))
    s += dados['idade']
    pessoas.append(dados.copy())
    dados.clear()
    while True:
        option = input('Quer continuar? [S/N] ').strip().upper()
        if option == 'S' or option == 'N':
            break
    if option == 'N':
        break

print('=-'*20)

print(f'A - Total de cadastros: {len(pessoas)} pessoas')
print(f'B - A média de idade é: {s/len(pessoas):.2f} anos.')
print(f'C - Mulheres cadastradas: ',end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(p['nome'],end=' ')
print('\nPessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] >= s/len(pessoas):
        for k, v in p.items():
            print(f'    {k} = {v} ',end=';')
        print()
print('\nFIM')