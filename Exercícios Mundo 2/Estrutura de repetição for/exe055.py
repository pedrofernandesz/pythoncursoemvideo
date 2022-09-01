# Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos. OBS: Sem usar listas, tuplas ou dict.

maior = 0
menor = 0

for c in range(1,6):
    weight = float(input(f'{c}° Peso: '))
    if c == 1:
        maior = weight
    else:
        if weight > maior:
            maior = weight
        elif weight < maior:
            menor = weight
    
print(f'Maior número digitado: {maior}kg')
print(f'Menor número digitado: {menor}kg')