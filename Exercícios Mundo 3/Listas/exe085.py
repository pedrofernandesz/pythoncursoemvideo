#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

numeros = [[],[]]
for c in range(0,7):
    number = int(input(f'Digite o {c}° valor: '))
    if number % 2 == 0:
        numeros[0].append(number)
    else:
        numeros[1].append(number)
        
numeros[0].sort()
numeros[1].sort()
print(f'Valores digitados: {numeros}')
print(f'Valores pares: {numeros[0]}')
print(f'Valores ímpares: {numeros[1]}')