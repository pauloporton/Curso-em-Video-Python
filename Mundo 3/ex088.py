from random import randint
from time import sleep
lista = []
jogos = [0, 0, 0, 0, 0, 0]
print('-=-'*12)
print(f'{'JOGO DA MEGA SENA':^35}')
print('-=-'*12)
n = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{' SORTEANDO JOGOS ':=^36}')
for l in range(0, n):
    for j in range(0, 6):
        sorteado = randint(1, 60)
        if sorteado not in jogos:
            jogos[j] = sorteado
    jogos.sort()
    lista.append(jogos[:])
    print(f'Jogo {l+1}: {lista[l]}')
    sleep(1)
print(f'{' BOA SORTE ':=^36}')

