print('-=-' * 10)
print('    10 TERMOS DE UMA PA')
print('-=-' * 10)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1
while c <= 10:
    print(a1, end=' -> ')
    a1 += r
    c += 1
print('PAUSA')
resp = 1
totn = 10
while resp != 0:
    c = 1
    resp = int(input('Deseja ver mais quantos termos dessa PA? '))
    if resp != 0:
        while c < resp + 1:
            print(a1, end=' -> ')
            a1 += r
            c += 1
            totn += 1
        print('PAUSA')
print('PROGRAMA ENCERRADO. Foram mostrados: {} TERMOS'.format(totn))
