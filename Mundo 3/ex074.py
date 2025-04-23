from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10),
           randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram: \n{numeros}')
print(f'O maior número é: {max(numeros)}')
print(f'O menor número é: {min(numeros)}')


