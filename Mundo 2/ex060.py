n = int(input('Digite um valor: '))
c = n
fatorial = 1
while c > 0:
    fatorial = fatorial * c
    print('{}'.format(c), end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    c += -1
print('{}! --> {}'.format(n, fatorial))
