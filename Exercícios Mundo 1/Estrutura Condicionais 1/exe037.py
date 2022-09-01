# Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

number = int(input('Digite um número inteiro: '))
print('''Digite a base de conversão:
[ 1 ] para binário
[ 2 ] para octal
[ 3 ] para hexadecimal''')
option = int(input('Digite 1, 2 ou 3: '))

if option == 1:
    print(f'{number} convertido para binário equivale a: {bin(number)[2:]}')
elif option == 2:
    print(f'{number} convertido para octal é: {oct(number)[2:]}')
elif option == 3:
    print(f'{number} convertido para hexadecimal é {hex(number)[2:]}')
else:
    print('Opção inválida')