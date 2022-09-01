'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

tupla = (int(input('Digite um número:')), int(input('Digite outro número: ')),
         int(input('Mais um número: ')), int(input('Outro número: ')))

print(f'O número 9 apareceu: {tupla.count(9)} vezes')

if tupla.count(3) == 0:
    print('Não foi digitado valor 3')
else:
    print(f'O valor 3 foi digitado pela primeira vez na posição: {tupla.index(3) + 1}')

cont = 0
print('Valores pares: ',end='')
for c in tupla:
    if c % 2 == 0:
        cont += 1
        print(c,end=' ')
if cont == 0:
    print('Nenhum')