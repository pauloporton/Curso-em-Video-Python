def ficha(nome= '<desconhecido>', gols= 0):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


#Programa principal
print('-='*20)
jogador = input('Nome do jogador: ')
n = input('Número de gols: ')
if jogador.strip() == '':
    jogador = '<desconhecido>'
if n.strip().isdigit():
    n = int(n)
else:
    n = 0

print(ficha(jogador, n))
