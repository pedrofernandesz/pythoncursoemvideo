times = ('Palmeiras', 'Corinthians', 'Flamengo','Fluminense','Athletico PR','Internacional','Atlético-MG','Red Bull Bragantino','América-MG','Santos','São Paulo','Botafogo','Goiás','Ceará SC','Coritiba','Avaí','Cuiabá','Atlético-GO','Fortaleza','Juventude')

print('Tabela do Brasileirão série A')
print('='*20)

while True:
    print('''[1] Ver os 5 primeiros colocados
[2] Ver os 4 últimos colocados
[3] Lista dos times em ordem alfabética
[4] Posição de um time
[5] Sair''')
    option = int(input('Opção: '))
    while option < 1 or option > 5:
        option = int(input('[ERRO] Opção inválida: '))
    print('='*40)
    if option == 1:
        for p, time in enumerate(times):
            if p < 5:
                print(f'{p+1}° {time}')
    elif option == 2:
        for p, time in enumerate(times):
            if p > 15:
                print(f'{p + 1}° {time}')
    elif option == 3:
        print(sorted(times))
    elif option == 4:
        optiontime = input('Posição de qual time? ').strip().capitalize()
        if times.count(optiontime) == 1:
            print('Este time não se encontra na tabela')
        else:
            print('A posição do time {} é: °{} colocado'.format(optiontime, times.index(optiontime) + 1))
    elif option == 5:
        break
    print('='*40)