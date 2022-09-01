# Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

name1 = input('Primeiro aluno: ').strip().capitalize()
name2 = input('Segundo aluno: ').strip().capitalize()
name3 = input('Terceiro aluno: ').strip().capitalize()
name4 = input('Quarto aluno: ').strip().capitalize()

lista = [name1,name2,name3,name4]
print(random.choice(lista))