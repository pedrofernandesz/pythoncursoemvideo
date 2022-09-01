#Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1

while c <= 20:
    print(primeiro, end=' -> ')
    primeiro = primeiro + r
    c = c + 1
print('Fim')