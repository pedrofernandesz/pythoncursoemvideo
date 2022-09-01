#Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

option = 'S'
s = quant = maior = menor = 0
while option == 'S':
    number = int(input('Digite um número: '))
    quant += 1
    s += number
    option = input('Quer continuar? [S/N] ').strip().upper()
    if quant == 1:
        maior = menor = number
    else:
        if number > maior:
            maior = number
        if number < menor:
            menor = number

print(f'Média: {s/quant:.2f}')
print(f'Maior: {maior}')
print(f'Menor: {menor}')