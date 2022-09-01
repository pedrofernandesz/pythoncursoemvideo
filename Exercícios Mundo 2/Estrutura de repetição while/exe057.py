#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input('Sexo: [F/M] ').upper().strip()
while 'M' != sexo != 'F':
    sexo = input('[ERRO] Opção inválida: ').upper().strip()
print('Dados inserido!')