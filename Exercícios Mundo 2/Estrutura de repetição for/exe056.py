#Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

s = 0
contfemale = 0
idadevelho = 0
nomevelho = ''

for c in range (1,5):
    name = input('Nome: ').strip()
    age = int(input('Idade: '))
    sexo = input('Sexo: [M - Masculino | F - Feminino] ').strip().upper()
    s += age
    while 'M' != sexo != 'F':
        sexo = input('Opção inválida: ').strip().upper()

    if sexo == 'M':
        if c == 1:
            idadevelho = age
        elif age > idadevelho:
            idadevelho = age
            nomevelho = name

    elif sexo == 'F' and age < 20:
        contfemale += 1
    

    print('-=' * 20)

print(f'Média de idades: {s/4:.1f}')
print(f'Homem mais velho do grupo é: {nomevelho} e tem {idadevelho} anos')
print(f'Quantidade de mulher com menos de vinte anos: {contfemale}')