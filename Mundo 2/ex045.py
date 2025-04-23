from random import choice
from time import sleep
# jogada do computador
jogadas = ['Pedra', 'Papel', 'Tesoura']
computador = choice(jogadas).lower()

# jogada do usuário
print('{:=^30}'.format(' JOKENPO '))
jogador = input('''Suas opções:
(Pedra) 
(Papel) 
(Tesoura)
Qual sua jogada? ''').lower()
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!')

# escolhas
print('-=-' * 10)
print('ESCOLHA DO JOGADOR: \033[4m{}\033[m'.format(jogador.capitalize()))
print('ESCOLHA DO COMPUTADOR: \033[4m{}\033[m'.format(computador.capitalize()))
print('-=-' * 10)

# resultado
if jogador == computador:
    print('EMPATE! Vamos jogar novamente?')
elif computador == 'pedra':
    if jogador == 'papel':
        print('VOCÊ GANHOU! Papel vence a pedra.')
    elif jogador == 'tesoura':
        print('VOCÊ PERDEU! Pedra vence a tesoura.')
    else:
        print('JOGADA INVÁLIDA! TENTE NOVAMENTE.')
elif computador == 'papel':
    if jogador == 'pedra':
        print('VOCÊ PERDEU! Papel vence a pedra.')
    elif jogador == 'tesoura':
        print('VOCÊ GANHOU! Tesoura vence o papel.')
    else:
        print('JOGADA INVÁLIDA! TENTE NOVAMENTE.')
elif computador == 'tesoura':
    if jogador == 'pedra':
        print('VOCÊ GANHOU! Pedra vence a tesoura.')
    elif jogador == 'papel':
        print('VOCÊ PERDEU! Tesoura vence o papel.')
    else:
        print('JOGADA INVÁLIDA! TENTE NOVAMENTE.')
print('-=-' * 10)








