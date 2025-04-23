inverso = ''
frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
for c in range(len(junto) - 1, -1, -1):
        inverso += junto[c]
print('O inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
        print('TEMOS UM PALÍNDROMO!')
else:
        print('NÃO TEMOS UM PALÍNDROMO.')