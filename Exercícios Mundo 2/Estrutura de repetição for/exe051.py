#Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = primeiro + (10 - 1) * r

for c in range(primeiro, decimo + r, r):
    print(c,end=' -> ')
    
print('Fim')