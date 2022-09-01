#Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.


price = float(input('Preço: '))
pricedesconto = price - ((price * 5)/100)
print(f'Valor original: R${price:.2f}')
print(f'Valor com desconto de 5% R${pricedesconto:.2f}')