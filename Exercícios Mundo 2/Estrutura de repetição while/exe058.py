#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

palpite = int(input('Qual seu palpite? '))
maquina = randint(0,10)
cont = 0

while palpite != maquina:
    if palpite > maquina:
        palpite = int(input('Menos... Tente mais uma vez: '))
    else:
        palpite = int(input('Menos... Tente mais uma vez: '))
    cont += 1

print(f'Parabéns você acertou com {cont} tentativas')