'''Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''
s = contmil = cont = 0
barato = ''
while True:
    product = input('Produto: ').strip().upper()
    price = float(input('Preço: R$'))
    option = input('Quer continuar? [S/N]').strip().upper()
    cont += 1
    s += price
    if price > 1000:
        contmil += 1
    if cont == 1 or price < barato:
        barato = price
        produtobarato = product
        
    print('-='*20)

    if option == 'N':
        break
print(f'Total gasto: R${s:.2f}')
print(f'Produtos com mais de R$1000: {contmil}')
print(f'Produto mais barato: {produtobarato} que custa R${barato:.2f}')