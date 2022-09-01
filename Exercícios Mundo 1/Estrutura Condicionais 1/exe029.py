#Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocity = float(input('Qual a velocidade do carro? '))
if velocity>80:
    multa = (velocity - 80) * 7
    print(f'Multado! Valor: R${multa:.2f}')
else:
    print('Boa viagem')