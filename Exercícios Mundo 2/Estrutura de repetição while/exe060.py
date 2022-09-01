''' Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120'''

number =int(input('Digite um número para ver seu fatorial: '))
fatorial = 1
while number > 0:
    if number > 1:
        print(f'{number}',end=' x ')
    else:
        print(f'{number}',end=' = ')
    fatorial = fatorial * number
    number -= 1
print(fatorial)