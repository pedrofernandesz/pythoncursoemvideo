''' Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para a [{l}, {c}]: '))
print('-='*40)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
print('-='*40)

spar = scoluna = 0

for c in matriz:
    for number in c:
        if number % 2 == 0:
            spar += number
for c in matriz:
    for number in c:
        if number == c[-1]:
            scoluna += number

print(f'A soma entre os valores pares é: {spar}')
print(f'A soma dos valores da terceira coluna é {scoluna}')
print(f'O maior valor da segunda linha: {max(matriz[1])}')