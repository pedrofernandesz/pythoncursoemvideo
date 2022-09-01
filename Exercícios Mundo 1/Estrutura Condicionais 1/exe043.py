'''
Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''

weight = float(input('Peso: '))
height = float(input('Altura: '))
imc = weight / height**2

if imc < 18.5:
    situation = 'ABAIXO DO PESO'
elif imc < 25:
    situation = 'PESO IDEAL'
elif imc < 30:
    situation = 'SOBREPESO'
elif imc < 40:
    situation = 'OBESIDADE'
else:
    situation = 'OBESIDADE MÓRBIDA'

print(f'Peso: {weight:.2f}kg')
print(f'Altura: {height:.2f}m')
print(f'IMC: {imc:.1f}')
print(f'Situação: {situation}')