'''
Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros

'''
#Recebe o valor da compra e a opção de pagamento
value = float(input('Valor da compra: '))
option = input('''[1] À vista dinheiro / cheque (OFF 10%)
[2] Cartão
Opção: ''').strip()


#Confere se a opção é válida
while option != '1' and option != '2':
    option = input('[ERRO] Opção inválida! Insira 1 ou 2: ').strip()

#Condição para opção 1
if option == '1':
    desconto = value*10/100
    valorfinal = value - desconto
    print(f'Valor da compra: R${value:.2f}')
    print(f'Desconto: R${desconto:.2f}')
    print(f'Valor a pagar: R${valorfinal:.2f}')

#Condição para opção diferente de 1, ou seja 2
else:

    #Opção de pagamento no débito ou crédito
    option2 = input('''[1] Débito (OFF 5%)
[2] Crédito
Opção: ''').strip()
    #Confere se a opção é válida
    while option2 != '1' and option2 != '2':
        option2 = input('[ERRO] Opção inválida! Insira 1 ou 2: ').strip()

    #Condição para opção 1
    if option2 == '1':
        desconto = value * 5 / 100
        valorfinal = value - desconto
        print(f'Valor da compra: R${value:.2f}')
        print(f'Desconto: R${desconto:.2f}')
        print(f'Valor a pagar: R${valorfinal:.2f}')
    
    #condição para opção 2
    else:
        print('AVISO: Divida em até 2x sem juros, 3x ou mais juros de 20%.')
        parcela = int(input('Parcela (até 12x): '))

        #Confere se a opção é válida
        while parcela < 1 or parcela > 12:
            parcela = int(input('Só aceitamos em até 12x: '))
        
        #Condição para parcela menor ou igual a 2
        if parcela <= 2:
            desconto = 0
            valorfinal = value - desconto
            print(f'Valor da compra: R${value:.2f}')
            print(f'Desconto: R${desconto:.2f}')
            print(f'Valor a pagar: R${valorfinal:.2f}')

        #condição para parcela maiores ou igual a 3
        else:
            
            juros = 20 * value / 100
            valorfinal = value + juros

            print(f'Valor da compra: R${value:.2f}')
            print(f'Juros: R${juros:.2f}')
            print(f'Parcelas: {parcela}x de {(valorfinal / parcela):.2f}')
            print(f'Valor a pagar: {valorfinal:.2f}')