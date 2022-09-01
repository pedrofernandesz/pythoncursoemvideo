#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

dados = dict()
gols = list()
s= 0
dados['nome'] = input('Nome do jogador: ').strip().capitalize()
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

for c in range (0,partidas):
    gols.append(int(input(f'    Quantos gols na partida {c}? ')))
    s += gols[c]
dados['gols'] = gols[:]
dados['total'] = s
print('=-'*40)
print(dados)
print('=-'*40)
for k, v in dados.items():
    print(f'O campo {k} tem o valor: {v}')
print('=-'*40)
print(f'O jogador: {dados["nome"]} fez {len(dados["gols"])} partidas')
for i ,v in enumerate(dados['gols']):
    print(f'    Na partida {i}, fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols')