#Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

number = 0
s = 0
cont = 0
while number != 999:
    number = int(input('Digite um número [999 para parar]: '))
    if number != 999:
        s += number
        cont += 1
print(f'A soma entre os {cont} números digitados é: {s}')