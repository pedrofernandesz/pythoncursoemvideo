#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
#Cria listas vazias
lista_jogos = list()
jogo = list()
#Pede ao usuário o número de jogos
jogos = int(input('Quantos jogos quer sortear? '))
#Estrutura de repetição que vai de 0 até x jogos
for c in range(0,jogos):
    #estrutura para sortear os 6 números para compor a lista jogo
    for n in range (1,7):
        #Verificação para saber se o número já foi digitado na lista, enquanto o número já se encontre na lista, fazer o sorteio novamente até achar um que não componhe a lista
        while True:
            #sortea um número entre 1 a 60
            sort = randint(1,60)
            if sort not in jogo:
                jogo.append(sort)
                break
    jogo.sort()
    lista_jogos.append(jogo[:])
    jogo.clear()

print(f'-=-=-=-= SORTEANDO {jogos} JOGOS -=-=-=-=')

for i ,j in enumerate(lista_jogos):
    print(f'Jogo {i+1}: {j}')
    sleep(1)
print('Boa sorte meu amigo!')