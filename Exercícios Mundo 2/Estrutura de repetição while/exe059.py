'''
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.

'''

number1 = int(input('Primeiro valor: '))
number2 = int(input('Segundo valor: '))
option = 0


while option != 5:
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair
''')
    option = int(input('Opção: '))
    while option < 1 or option > 5:
        option = int(input('[ERRO] digite uma opção válida: '))
    if option == 1:
        print(f'{number1} + {number2} = {number1 + number2}')
    elif option == 2:
        print(f'{number1} x {number2} = {number1 * number2}')
    elif option == 3:
        if number1 > number2:
            print(f'Maior número: {number1}')
        else:
            print(f'Maior número: {number2}')
    elif option == 4:
        number1 = int(input('Digite novamente o primeiro número: '))
        number2 = int(input('Segundo número novamente: '))
    print('-=' * 20)