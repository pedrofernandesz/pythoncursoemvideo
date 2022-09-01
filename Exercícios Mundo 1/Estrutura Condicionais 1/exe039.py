# Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

nasc = int(input('Nascimento: '))
anoatual = date.today().year
idade = anoatual - nasc

if idade == 18:
    print('Aliste-se imediatamene.')
elif idade < 18:
    saldo = 18 - idade
    print(f'Seu alistamento será em {saldo} anos no ano de {anoatual + saldo}')
else:
    saldo = idade - 18
    print(f'Seu alistamento foi em {anoatual - saldo} há {saldo} anos atrás')