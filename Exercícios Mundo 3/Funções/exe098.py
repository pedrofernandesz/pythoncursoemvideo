'''Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''

def contador (i,f,p):
    from time import sleep
    cont = 0
    print('-='*20)
    print(f'Contagem de {i}, até {f} em {p} e {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}',end=' ')
            sleep(1)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}',end=' ')
            sleep(1)
            cont -= p
        print('FIM!')

contador(1,10,1)
contador(10,0,2)
print('Agora é sua vez: ')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i,f,p)