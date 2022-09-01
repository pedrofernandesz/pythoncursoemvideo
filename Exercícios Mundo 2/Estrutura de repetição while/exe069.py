'''Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''

larger = contmale = cont_female_less_than = 0
while True:
    age = int(input('Idade: '))
    sexo = ''
    while sexo != 'M' and sexo != 'F':
        sexo = input('Sexo: [M/F] ').strip().upper()
    if age > 18:
        larger += 1
    if sexo == 'M':
        contmale += 1
    if sexo == 'F' and age < 20:
        cont_female_less_than += 1
    option = input('Quer continuar? [S/N] ').strip().upper()
    print('-='*20)
    if option == 'N':
        break
print('Fim do programa!')
print(f'Maiores que 18 anos: {larger}')
print(f'Quantidade de homens cadastrados: {contmale}')
print(f'Quantidade de mulheres com menos de 20 anos: {cont_female_less_than}')