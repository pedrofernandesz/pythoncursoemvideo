#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano=0):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return 'NEGADO'
    elif idade < 18 or idade > 65:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'

date = int(input('Nascimento: '))
print(voto(date))