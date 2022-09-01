# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import time
import random

print('Irei pensar em um número')
print('...')
time.sleep(1)
numero = random.randint(0, 5)
o = int(input('Qual número eu pensei? '))
if o == numero:
    print('Parabéns você acertou, número {}'.format(numero))
else:
    print('Você errou, número {}'.format(numero))