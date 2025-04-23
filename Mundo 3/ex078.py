num = []
max = 0
min = 0
for c in range(0, 5):
    num.append(int(input(f'Digite um valor para a {c + 1}ª posição: ')))
    if c == 0:
        min = num[c]
    if num[c] > max:
        max = num[c]
    elif num[c] < min:
        min = num[c]
print('-=-' * 15)
print(f'Você digitou os valores: {num}')
print(f'O maior valor digitado foi {max}, nas posições ', end='')
for pos, v in enumerate(num):
    if v == max:
        print(f'{pos + 1}... ', end='')
print()
print(f'O menor valor digitado foi {min} nas posições ', end='')
for pos, v in enumerate(num):
    if v == min:
        print(f'{pos + 1}... ', end='')


