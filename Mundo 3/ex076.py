lista = ('Lápis', 1.57,
         'Caderno', 18.30,
         'Borracha', 1.30,
         'Compasso', 9.25,
         'Marca-texto', 6.75,
         'Livro', 35.50,
         'Apontador', 7.30)
print('-'*30)
print(f'{'LISTAGEM DE PREÇOS':^30}')
print('-'*30)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<23}', end='')
    else:
        print(f'R${lista[pos]:>5.2f}')
print('-'*30)

