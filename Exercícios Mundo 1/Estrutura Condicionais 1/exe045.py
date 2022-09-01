# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você, sem usar listas, tuplas ou dict.

from time import sleep
from random import randint

print('''[1] PEDRA
[2] PAPEL
[3] TESOURA
''')

maquina = randint(1,3)
option = int(input('Jogada: '))
while option < 1 or option > 3:
    option = int(input('[ERRO] Digite uma opção válida: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')

if option == maquina:
    print('EMPATE!')

elif option == 1 and maquina == 3:
    print('Você venceu!')
elif option == 2 and maquina == 1:
    print('Você venceu!')
elif option == 3 and maquina == 2:
    print('Você venceu!')
else:
    print('Você perder')