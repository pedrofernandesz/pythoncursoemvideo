#Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. 

while True:
    number = int(input('Quer ver a tabuada de qual valor? '))
    if number < 0:
        break
    for c in range (0,11):
        print(f'{number} X {c} = {number * c}')
    print('-='*20)
print('Programa finalizado')