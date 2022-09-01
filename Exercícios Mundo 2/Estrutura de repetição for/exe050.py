#Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
s = 0
cont = 0
for c in range (1,7):
    number = int(input(f'Digite o {c}° inteiro: '))
    if number % 2 == 0:
        cont += 1
        s += number
print(f'A soma entre os {cont} números pares digitado é: {s}') 