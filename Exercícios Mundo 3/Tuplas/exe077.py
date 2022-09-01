#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais. 

palavras = ('aprender', 'programar', 'linguaguem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos: ',end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'{letra.lower()}', end=' ')