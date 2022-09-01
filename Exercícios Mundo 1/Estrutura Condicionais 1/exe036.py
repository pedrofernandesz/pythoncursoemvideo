#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valorcasa = float(input('Valor da casa: R$'))
salary = float(input('Salário: R$'))
ano = int(input('Em quantos anos vai pagar: '))
prestacao = valorcasa / (ano*12)
print(f'''Valor da casa: R${valorcasa:.2f}
Dividido em R${prestacao:.2f} de {ano*12} vezes em {ano} anos
''')
minimo = salary * 30 / 100

if prestacao <= minimo:
    print('Empréstimo aprovado!')
else:
    print('Esmpréstimo negado!')