def ficha(name='<desconhecido>', gols=0):
    print(f'O jogador {name} fez {gols} gol(s) no campeonato')

name = input('Nome: ').strip().capitalize()
gols = input('Gols: ').strip()
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if name == '':
    ficha(gols=gols)
else:
    ficha(name, gols)