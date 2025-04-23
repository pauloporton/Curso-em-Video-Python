numeros = (int(input('Digite um valor: ')),
           int(input('Digite outro valor: ')),
           int(input('Digite mais um valor: ')),
           int(input('Digite o último valor: ')))
print('-=-'*10)
print(f'Você digitou os valores: {numeros}')
print('-=-'*10)
print(f'O valor 9 foi digitado {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 foi digitado na {numeros.index(3) + 1}ª posição')
else:
    print(f'O valor 3 não foi digitado.')
print('Os valores pares digitados foram: ', end='')
for c in range(0, len(numeros)):
    if numeros[c] % 2 == 0:
        print(numeros[c], end=', ')

