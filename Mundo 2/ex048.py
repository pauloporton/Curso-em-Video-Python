soma = 0
cont = 0
print('Os números ímpares múltiplos de 3 no intervalo de 1 até 500 são: ')
for c in range(0, 501, 3):
    if c % 2 != 0:
        print(c, end=' ')
        soma += c
        cont += 1
print()
print('A soma entre os {} números vale: {}'.format(cont, soma))
