maior = 0
menor = 0
n1 = int(input('Digite o 1° valor: '))
if n1 > maior:
    maior = n1
if n1 < menor or menor == 0:
    menor = n1
n2 = int(input('Digite o 2° valor: '))
if n2 > maior:
    maior = n2
if n2 < menor:
    menor = n2
n3 = int(input('Digite o 3° valor: '))
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3
print('ANALISANDO...')
print('O maior número é: {}'.format(maior))
print('O menor número é: {}'.format(menor))

