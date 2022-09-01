#Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO". OBS: Sem usar estrutura de decisão.

city = input('Digite a cidade em que você nasceu: ').strip().upper()

print(city[:5] == 'SANTO')