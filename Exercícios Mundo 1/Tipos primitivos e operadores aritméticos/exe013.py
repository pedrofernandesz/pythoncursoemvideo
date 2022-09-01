# Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salary = float(input('Salário R$'))
newsalary = ((salary * 15) / 100) + salary
print(f'O salário de R${salary:.2f} reajustado para R${newsalary:.2f}, aumento de 15%')