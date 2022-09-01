#Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro = int(input('Primeiro termo: '))
termo = primeiro
r = int(input('Razão: '))
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print(f'{termo} -> ', end='')
        termo = termo + r
        c = c + 1

    print('Pausa')     
    mais = int(input('Quantos termos mostrar mais? '))      
print('Fim')