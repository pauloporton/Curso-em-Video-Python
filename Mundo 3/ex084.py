lista = []
dado = []
maxi = 0
mini = 0
while True:
    dado.append(input('Nome: '))
    dado.append(float(input("Peso(kg): ")))
    if len(lista) == 0:
        maxi = mini = dado[1]
    else:
        if dado[1] > maxi:
            maxi = dado[1]
        if dado[1] < mini:
            mini = dado[1]
    lista.append(dado[:])
    dado.clear()
    while True:
        resp = input('Quer continuar? (S/N) ').strip().upper()
        if resp not in 'SN':
            print('TENTE NOVAMENTE.', end=' ')
        else:
            break
    if resp == 'N':
        break

print('-=-'*15)
print(f'Ao todo, você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {maxi}kg. Peso de: ', end='')
for v in lista:
    if v[1] == maxi:
        print(f'[{v[0]}]', end=' ')
print()
print(f'O menor peso foi de {mini}kg. Peso de: ', end='')
for c in lista:
    if c[1] == mini:
        print(f'[{c[0]}]', end=' ')
print()




