#Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint

def sorteia(lista):
    """
        Sorteia 5 número para jogar dentro da lista
        :param lista:Lista para ser inserido os valores sorteados

    """
    print('Sorteando 5 valores: ',end='')
    for c in range(0,5):
        sort = randint(0,10)
        print(sort,end=' ')
        lista.append(sort)
    print('Feito')

def somarPar(lista):
    s = 0
    for c in  lista:
        if c % 2 == 0:
            s += c
    print(f'Somando os valores {lista} = {s}')

number = list()
sorteia(number)
somarPar(number)
help(sorteia)