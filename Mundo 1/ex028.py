import random
aleatorio = random.randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-' * 20)
n = int(input('Em que número eu pensei? '))
if n == aleatorio:
    print('VOCÊ ACERTOU!')
else:
    print('VOCÊ ERROU! pensei no número: {}'.format(aleatorio))



