#Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input('Digite uma frase: ').strip().lower()

print('A letra "A" aparece {} vezes'.format(frase.count('a')))
print('A letra "A" aparece pela primeira vez na posição: {}'.format((frase.find('a') + 1)))
print('A letra "A" aparece pela última vez na posição: {}'.format((frase.rfind('a') + 1)))