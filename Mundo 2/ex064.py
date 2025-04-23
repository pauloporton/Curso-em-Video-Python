n = 1
tot = 0
soma = 0
while n != 999:
    n = int(input('Digite um valor (digite 999 para encerrar): '))
    if n != 999:
        tot += 1
        soma += n
print('A soma entre os {} valores é igual a: {}'.format(tot, soma))




