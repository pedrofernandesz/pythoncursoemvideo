# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
cont = 0
while True:
    jogador = int(input('Número: '))
    option = input('Par ou ímpar? [P/I] ').strip().upper()
    pc = randint(1,10)
    print(f'Você jogou {jogador} e o computador {pc} = {jogador + pc}')
    print('-'*20)
    if option == 'P':
        if (jogador + pc) % 2 == 0:
            print('Você venceu!')
            cont += 1
            print('Vamos jogar novamente!')
            print('=-'*20)
        else:
            print('Você perdeu')
            break
    else:
        if (jogador + pc) % 2 != 0:
            print('Você venceu!')
            cont += 1
            print('Vamos jogar novamente!')
            print('=-'*20)
        else:
            print('Você perdeu!')
            break
print(f'Você venceu {cont} seguidas')