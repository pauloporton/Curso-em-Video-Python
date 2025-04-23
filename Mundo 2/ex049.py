from time import sleep
# lendo o valor
n = int(input('Digite um valor: '))
print('Gerando tabuada...')
print()
sleep(1.5)

# tabuada
print('{:=^30}'.format(' TABUADA DO {} '.format(n)))
for c in range(1,11):
    print('{} x {} = {}'.format(n, c, n * c))
print('{:=^30}'.format(' FIM DA TABUADA '))

