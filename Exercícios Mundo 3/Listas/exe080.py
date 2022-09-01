#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = list()

for c in range(0,5):
    number = int(input(f'Digite o {c+1}° número: '))
    if c == 0 or number > lista[-1]:
        lista.append(number)
        print(f'Valor adcionado na posição: {lista.index(number)}')
    else:
        pos = 0
        while pos < len(lista):
            if number <= lista[pos]:
                lista.insert(pos,number)
                print(f'Valor adcionado na posição: {lista.index(number)}')
                break
            pos += 1 
                
print(f'Valores digitados: {lista}')