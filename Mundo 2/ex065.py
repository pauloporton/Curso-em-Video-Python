r = 'S'
tot = 0
soma = 0
maior = 0
menor = 0
while r == 'S':
    n = int(input('Digite um valor: '))
    tot += 1
    soma += n
    if tot == 1:
        menor = maior = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    r = input('Quer continuar? (S/N) ').upper().strip()
media = soma / tot
print('A média entre os {} valores digitados é: {:.2f}'.format(tot, media))
print('O maior valor é {} e o menor é {}'.format(maior, menor))


