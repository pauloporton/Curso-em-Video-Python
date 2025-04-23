jogador = {}
gols = []
totgols = 0
jogador['nome'] = input('Nome do jogador: ')
n = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
for c in range(0, n):
    g = int(input(f'Quantos gols na {c+1}ª partida? '))
    gols.append(g)
    totgols += g
jogador['gols'] = gols
jogador['total'] = totgols
print('-='*20)
print(f'O jogador {jogador["nome"]} jogou {n} partidas.')
for cont in range(0, n):
    print(f'    => Na {cont+1}ª partida, fez {gols[cont]} gols')
print(f'Foi um total de {totgols} gols')
