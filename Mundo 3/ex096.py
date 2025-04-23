def area(a, b):
    a = a * b
    print(f'A área de um terreno {l} x {c} é: {a}m²')



print('Controle de terrenos')
print('-'*20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
print('-'*20)
area(l, c)
