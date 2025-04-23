print('-=-'*10)
print('    LOJAS SUPER BARATÃO')
print('-=-'*10)
total = 0
mil = 0
barato = 0
nomebarato = ''
while True:
    produto = input('Nome do produto: ')
    valor = float(input('Valor: R$'))
    total += valor
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? (S/N) ').upper().strip()[0]
    if valor > 1000:
        mil += 1
    if barato == 0 or valor < barato:
        barato = valor
        nomebarato = produto
    if resp[0] == 'N':
        break
print('-------- FIM DO PROGRAMA --------')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomebarato}, custando R${barato:.2f}')


