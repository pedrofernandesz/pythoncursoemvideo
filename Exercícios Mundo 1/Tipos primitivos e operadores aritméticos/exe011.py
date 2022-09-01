# Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Largura: '))
altura = float(input('Altura: '))
area = largura * altura
print('Dimensão {largura}x{altura} com área de {area}m²')
print(f'Levando em consideração que cada litro de tinta pinta uma área de 2m², vai haver o gasto de {area/2} litros de tinta')