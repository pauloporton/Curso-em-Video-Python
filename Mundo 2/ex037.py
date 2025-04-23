n = int(input('Digite um valor inteiro: '))
print('=-='*10)
escolha = int(input('''Digite {1} para BINÁRIO
Digite {2} para OCTAL
Digite {3} para HEXADECIMAL 
'''))
print('=-='*10)
if escolha == 1:
    print('{} convertido para BINÁRIO é: {}'.format(n, bin(n)[2:]))
elif escolha == 2:
    print('{} convertido para OCTAL é: {}'.format(n, oct(n)[2:]))
elif escolha == 3:
    print('{} convertido para HEXADECIMAL é: {}'.format(n, hex(n)[2:]))
else:
    print('Valor inválido!')
