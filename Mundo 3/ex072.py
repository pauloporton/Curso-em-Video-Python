extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
resp = ''
while True:
    while True:
        n = int(input('Digite um valor de 0 a 20: '))
        if 0 <= n <= 20:
            break
        print('TENTE NOVAMENTE. ', end = '')
    print(f'Você digitou o número \033[4m{extenso[n]}\033[m')
    while True:
        resp = input('Quer continuar? (S/N) ').strip().upper()
        if resp not in 'SN':
            print('TENTE NOVAMENTE.', end=' ')
        else:
            break
    if resp == 'N':
        break
print('FIM DO PROGRAMA.')


