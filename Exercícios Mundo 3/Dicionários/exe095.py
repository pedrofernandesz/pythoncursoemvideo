#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogadores = list()
dados = dict()
gols = list()

while True:
    s = 0
    gols.clear()
    dados.clear()
    dados['nome'] = input('Nome do jogador: ').strip().capitalize()
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    for c in range (0,partidas):
        gols.append(int(input(f'    Quantos gols na partida {c+1}? ')))
        s += gols[c]
    dados['gols'] = gols[:]
    dados['total'] = s
    jogadores.append(dados.copy())
    while True:
        option = input('Quer continuar? [S/N] ').strip().upper()
        if option == 'S' or option == 'N':
            break
    if option == 'N':
        break
print('=-'*30)

print(f'{"cod":<4}{"Nome":<10}{"Gols":<18}{"Total"}')
print('-'*60)
for i ,j in enumerate(jogadores):
    print(f'{i:<4} {j["nome"]:<10}{str(j["gols"]):<18}{j["total"]}')
while True:
    print('-'*60)
    option = int(input('Mostrar dados de qual jogador? (999 para finalizar) '))
    if option == 999:
        break
    while option > len(jogadores) or option < 0:
        option = int(input('Jogador inexistente - '))
    print(f'  -  Levantamento do jogador {jogadores[option]["nome"]}')
    for i, g in enumerate(jogadores[option]['gols']):
        print(f'    No jogo {i+1} fez {g} gols.')
print('Programa finalizado!')