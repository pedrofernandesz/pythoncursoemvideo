#Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

extensos = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
            'sete', 'oito',
            'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
            'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    number = int(input('Digite um número de 0 a 20 para ver seu extenso: '))
    if 0 <= number <= 20:
        break


print(f'O número {number} é escrito: {extensos[number]}')