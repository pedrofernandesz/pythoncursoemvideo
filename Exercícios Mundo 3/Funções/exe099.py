def maior(*num):
    maior =  0
    print('-='*30)
    for i, n in enumerate(num):
        print(f'{n}',end=' ')
        if i <= 1 or n > maior:
            maior = n
    print(f'Foram informados {len(num)} valores')
    print(f'O maior valor informado foi: {maior}')

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()