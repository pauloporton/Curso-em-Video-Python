def fatorial(num, show=False):
    """
    => Calcula o fatorial de um número
    :param num: O número a ser calculado
    :param show: (opcional) Mostra ou não a conta do número n
    :return: O valor do fatorial do número n
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            if c>1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end='')
        f *= c
    return f


n = int(input('Digite um valor: '))
print(fatorial(n, True))


