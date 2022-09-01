'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
'''
from datetime import date

birth = int(input('Nascimento: '))
age = date.today().year - birth

if age <= 9:
    category = 'MIRIM'
elif age <= 14:
    category = 'INFANTIL'
elif age <= 19:
    category = 'JÚNIOR'
elif age <= 25:
    category = 'SÊNIOR'
else:
    category = 'MASTER'

print(f'Age: {age} years')
print(f'Category: {category}')