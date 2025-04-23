def moeda(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def aumentar(valor = 0, taxa = 0, formatar = False):
    res = valor + (valor * taxa/100)
    if formatar:
        return  moeda(res)
    else:
        return res


def diminuir(valor = 0, taxa = 0, formatar = False):
    res = valor - (valor * taxa/100)
    if formatar:
        return moeda(res)
    else:
        return res


def dobro(valor = 0, formatar = False):
    res = valor * 2
    if formatar:
        return moeda(res)
    else:
        return res


def metade(valor = 0, formatar = False):
    res = valor / 2
    if formatar:
        return moeda(res)
    else:
        return res


def resumo(valor = 0, taxaAum = 0, taxaDim = 0):
    print('-'*30)
    print(f'{" RESUMO DO VALOR ":^30}')
    print('-'*30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{taxaAum}% de aumento: \t{aumentar(valor, taxaAum, True)}')
    print(f'{taxaDim}% de redução: \t{diminuir(valor, taxaDim, True)}')
    print('-'*30)
