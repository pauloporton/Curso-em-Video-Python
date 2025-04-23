from random import randint
aleatorio = randint(0, 10)
print('-=-' * 20)
print('Vou pensar em um número de 0 a 10. Tente adivinhar...')
print('-=-' * 20)
n = int(input('Em que número eu pensei? '))
totvezes = 1
while n != aleatorio:
    if n > aleatorio:
        n = int(input('MENOS! Tente novamente: '))
    else:
        n = int(input('MAIS! Tente novamente: '))
    totvezes += 1
if n == aleatorio:
    print('PARABÉNS!! Você acertou na {}° tentativa!'.format(totvezes))


