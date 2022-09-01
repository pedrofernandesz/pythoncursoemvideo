#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

dados = dict()

dados['name'] = input('Nome: ')
dados['media'] = float(input('Média: '))


if dados['media'] >= 7:
    dados['situation'] = 'Aprovado'
elif 5 <= dados['media'] < 7:
    dados['situation'] = 'Recuperação'
elif dados['media'] < 5:
    dados['situation'] = 'Reprovado'


print('='*40)
for k, v in dados.items():
    print(f'O campo {k} tem valor: {v}')