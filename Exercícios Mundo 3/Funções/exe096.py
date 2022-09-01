#Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def form (msg):
    print('='*40)
    print(f'{msg:^40}')
    print('='*40)
def aterr (largura, comprimento):
    a = (largura * comprimento)
    print(f'A área das dimensões: {largura}m por {comprimento}m é: {a}m²')

form('Controle de Terrenos')
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
aterr(l,c)