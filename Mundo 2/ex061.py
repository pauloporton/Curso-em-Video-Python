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
print('FIM')
