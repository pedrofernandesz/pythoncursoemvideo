#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date, datetime

dados = {'nome':input('Nome: ').strip().capitalize(),
         'idade': date.today().year - (int(input('Ano de nascimento: '))),
         'ctps':int(input('Carteira de trabalho: (0 não tem)'))
         }

if dados['ctps'] != 0:
    dados['contratatacao'] = int(input('Ano de contrato: '))
    dados['salario'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratatacao'] + 35) - datetime.now().year)

print('-'*40)

for k, v in dados.items():
    print(f'  -  O campo {k} tem valor: {v}')