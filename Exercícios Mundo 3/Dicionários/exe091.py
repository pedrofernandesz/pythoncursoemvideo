#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from audioop import reverse
from operator import itemgetter
from random import randint
from time import sleep

jogadores = dict()

for c in range(1,5):
    jogadores[f'jogador{c}'] = randint(1,6)

for k, v in jogadores.items():
    print(f'{k} tirou: {v} no dado')
    sleep(1)

print('-='*20)

cont = 0
for k ,v in sorted(jogadores.items(), key=itemgetter(1), reverse=True):
    cont += 1
    print(f'{cont}° Lugar: {k} dado {v}')
