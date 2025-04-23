matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]
somapar = 0
soma2c = 0
mai2l = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if c == 2:
            soma2c += matriz[l][c]
        if l == 1:
            if matriz[l][c] > mai2l or c==0:
                mai2l = matriz[l][c]
print('-=-'*15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=-'*15)
print(f'A soma dos valores pares é: {somapar}')
print(f'A soma dos valores da coluna 2 é: {soma2c} ')
print(f'O maior valor da linha 1 é: {mai2l}')


