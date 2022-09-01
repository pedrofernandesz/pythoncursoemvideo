#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salary = float(input('Salário: R$'))
if salary > 1250:
    salaryaumentado = (salary * 10 / 100) + salary
else:
    salaryaumentado = (salary * 15 / 100) + salary
print(f'Salário de R${salary:.2f} aumentado para R${salaryaumentado:.2f}')