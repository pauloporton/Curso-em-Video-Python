listageral = []
listapar = []
listaimpar = []
resp = ''
while True:
    listageral.append(int(input('Digite um valor: ')))
    while True:
        resp = input('Quer continuar? (S/N) ').strip().upper()
        if resp not in 'SN':
            print('TENTE NOVAMENTE. ', end='')
        else:
            break
    if resp == 'N':
        break
listageral.sort()
for c in range(0, len(listageral)):
    if listageral[c] % 2 == 0:
        listapar.append(listageral[c])
    else:
        listaimpar.append(listageral[c])
listapar.sort()
listaimpar.sort()
print('-=-'*15)
print(f'TODOS OS VALORES: {listageral}')
print(f'VALORES PARES: {listapar}')
print(f'VALORES ÍMPARES: {listaimpar}')


