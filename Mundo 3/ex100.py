from random import randint
from time import sleep
numeros = []

def sorteia():
    print('Sorteando os 5 valores da lista: ', end='')
    for c in range(0, 5):
        numeros.append(randint(1, 10))
        print(numeros[c], end=' ')
        sleep(0.5)
    print('PRONTO!')
    

def somapar():
    soma = 0
    for v in range(0, len(numeros)):
        if numeros[v] % 2 == 0:
            soma += numeros[v]
    print(f'Somando os valores pares de {numeros} temos: {soma}')



sorteia()
somapar()