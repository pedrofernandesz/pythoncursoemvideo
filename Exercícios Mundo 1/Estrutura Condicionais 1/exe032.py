#Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import datetime

year = int(input('Digite o ano: [0 para analisar o ano atual] '))

if year == 0:
    year = datetime.date.today().year

if year % 4 ==0 and year % 100 != 0 or year % 400 == 0:
    print(f'{year} é um ano bissexto')

else:
    print(f'{year} não é um ano bissexto')