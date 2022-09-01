#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = list()
while True:
    number = int(input(f'Digite um número: '))
    if lista.count(number) == 1 and len(lista) > 0:
        print('Valor duplicado, não vou adcionar')
    else:
        lista.append(number)
        print('Valor adcionado')
    option = input('Quer continuar? [S/N] ').strip().upper()
    if option == 'N':
        break
print('-='*40)
lista.sort()
print(f'Você digitou os valores: {lista}')