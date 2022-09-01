#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.


days = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Informe os km rodado com este carro: ' ))
pagar = (60*days) + (0.15 * km)
print(f'Valor a pagar R${pagar:.2f}')
