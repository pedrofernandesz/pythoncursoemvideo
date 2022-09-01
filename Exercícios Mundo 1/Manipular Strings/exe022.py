'''
Nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.

'''

name = input('Digite um nome completo: ').strip()
print(name.upper())
print(name.lower())
print('Total de letras: {}'.format(len(name) - name.count(' ')))
print('Total de letras do primeiro nome: {}'.format(len(name.split()[0])))