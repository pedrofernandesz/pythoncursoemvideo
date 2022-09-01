'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = list()
while True:
    number = int(input('Digite um número: '))
    lista.append(number)
    while True:
        option = input('Quer continuar? [S/N] ').strip().upper()
        if option == 'S' or option == 'N':
            break
    if option == 'N':
        break
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Valores em forma decrescente: {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi digitado e não está na lista.')