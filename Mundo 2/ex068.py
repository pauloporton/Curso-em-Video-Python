from random import randint
ganhadas = 0
print('-=-'*10)
print('  VAMOS JOGAR PAR OU ÍMPAR')
print('-=-'*10)
while True:
    jogador = int(input('Jogue um valor: '))
    computador = randint(0, 10) #"jogada" do computador
    soma = jogador + computador #soma da jogada do computador e do jogador
    escolha = ' '
    while escolha not in 'PI':
        escolha = input('Par ou Ímpar? (P/I) ').upper().strip()[0]
    if soma % 2 == 0: #verificar se o valor é par ou ímpar
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    print('---'*10)
    print(f'Você jogou {jogador} e o computador jogou {computador} \nSOMA = {soma} / DEU {resultado}')
    print('---'*10)
    if resultado[0] != escolha[0]: #para o looping se o jogador perde
        break
    print('VOCÊ VENCEU!! \nVamos jogar novamente...')
    ganhadas += 1 #contabiliza as partidas vencidas pelo jogador
    print('-=-'*10)
if ganhadas == 1:
    print(f'GAME OVER! Você venceu 1 vez.')
else:
    print(f'GAME OVER! Você venceu {ganhadas} vezes.')



