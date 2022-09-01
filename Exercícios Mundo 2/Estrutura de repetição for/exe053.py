#Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
print(f'Frase: {junto}')
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
if inverso == junto:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')

print(f'{junto} -> {inverso}')