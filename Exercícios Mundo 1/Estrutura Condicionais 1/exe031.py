#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

viagem = float(input('Digite a distância da viagem em KM: '))
print(f'Viagem: {viagem:.1f}KM')
if viagem <= 200:
    valor = viagem * 0.50
else:
    valor = viagem * 0.45
print(f'Valor: R${valor:.2f}')