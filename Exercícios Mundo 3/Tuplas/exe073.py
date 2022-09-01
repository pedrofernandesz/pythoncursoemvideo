'''Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.'''


times = ('Palmeiras', 'Corinthians', 'Flamengo','Fluminense','Athletico PR','Internacional','Atlético-MG','Red Bull Bragantino','América-MG','Santos','São Paulo','Botafogo','Goiás','Ceará SC','Coritiba','Avaí','Cuiabá','Atlético-GO','Fortaleza','Juventude', 'Chapecoense')

print('Listas de tima do Brasileirão série A')
for cont in range(0, len(times)):

    print(f'{cont+1}° {times[cont]}')

print('=-'*20)
print(f'5 primeiros: {times[:5]}')
print('-'*40)
print(f'4 últimos colocados: {times[-4:]}')
print('-'*40)
print(f'Times em ordem alfbética: {sorted(times)}')
print('-'*40)
if 'Chapecoense' in times:
    print('Chapecoence se encontra na posição: {}'.format(times.index('Chapecoense')+1))
else:
    print('Chapecoense não é da série A')