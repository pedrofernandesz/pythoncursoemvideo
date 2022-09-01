#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

numeros = list()
par = list()
impar = list()
while True:
    number = int(input('Digite um número: '))
    numeros.append(number)
    while True:
        option = input('Quer continuar? [S/N] ').strip().upper()
        if option == 'S' or option == 'N':
            break
    if option == 'N':
        break
for n in numeros:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(f'Lista completa: {numeros}')
print(f'Lista de números pares: {par}')
print(f'Lista de números ímpares: {impar}')