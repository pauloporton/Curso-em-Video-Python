jogadores = []
jogador = {}
gols = []
cont = 0
while True:
    print('-='*20)
    totgols = 0
    jogador['nome'] = input('Nome do jogador: ')
    n = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    for c in range(0, n):
        g = int(input(f'Quantos gols na {c + 1}ª partida? '))
        gols.append(g)
        totgols += g
    jogador['gols'] = gols[:]
    gols.clear()
    jogador['total'] = totgols
    jogadores.append(jogador.copy())

    while True:
        resp = input('Quer continuar? (S/N) ').strip().upper()
        if resp not in 'SN':
            print('TENTE NOVAMENTE.', end= ' ')
        else:
            break
    if resp == 'N':
        break

print('-='*20)
print(f'{"cod":<5} {"nome":<12} {"gols":<15} {"total":<10}')
print('-='*20)
for v in jogadores:
    print(f'{cont:<5} {v["nome"]:<12} {v["gols"]} {v["total"]:>10}')
    cont += 1

while True:
    print('-='*20)
    j = int(input('Mostrar dados de qual jogador? '))
    if j == 999:
        break
    if j > len(jogadores):
        print(f'ERRO. Não existe jogador com o número {j}! Tente novamente.')
    print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[j]["nome"]}')
    for l in range(0, len(jogadores[j]["gols"])):
        print(f'    => Na {l+1}ª partida, fez {jogadores[j]["gols"][l]}')
print('<<< VOLTE SEMPRE >>>')



