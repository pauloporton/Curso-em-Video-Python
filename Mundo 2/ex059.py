n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
maior = n1
menor = n2
r = 1
while r != 5:
    if n2 > n1:
        maior = n2
        menor = n1
    r = int(input('''=======================================
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa
    O que você deseja fazer com {} e {}? '''.format(n1, n2)))
    print('=======================================')
    if r == 1:
        print('resposta: {} + {} = {}'.format(n1, n2, n1 + n2))
    elif r == 2:
        print('resposta: {} X {} = {}'. format(n1, n2, n1 * n2))
    elif r == 3:
        if n1 == n2:
            print('resposta: Os dois valores são iguas! ')
        else:
            print('resposta: O número {} é maior do que {}'. format(maior, menor))
    elif r == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif r > 5 or r < 1:
        print('VALOR INVÁLIDO! tente novamente')
print('PROGRAMA ENCERRADO')


