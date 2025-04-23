print('-=-' * 10)
print('    10 TERMOS DE UMA PA')
print('-=-' * 10)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
ultimo = a1 + (10 -1) * r
for c in range(a1, ultimo + r , r):
    print(c, end=' -> ')
print('FIM')