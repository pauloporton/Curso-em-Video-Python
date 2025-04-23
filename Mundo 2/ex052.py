totdiv = 0
n = int(input('Digite um valor: '))
for c in range(n, 0, -1):
    div = n % c
    if div == 0:
        totdiv += 1
if totdiv == 2:
    print('O valor {} É PRIMO!'.format(n))
else:
    print('O valor {} NÃO É PRIMO, pois tem {} divisores'.format(n, totdiv))


