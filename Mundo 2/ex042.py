r1 = int(input('Digite o valor do 1° segmento de reta: '))
r2 = int(input('Digite o valor do 2° segmento de reta: '))
r3 = int(input('Digite o valor do 3° segmento de reta: '))
if r1 + r2 <= r3 or r1 + r3 <= r2 or r2 + r3 <= r1:
    print('NÃO é possível formar um triângulo!')
elif r1 == r2 == r3:
    print('É possível formar um triângulo EQUILÁTERO!')
elif r1 == r2 or r1 == r3 or r2 == r3:
    print('É possível formar um triângulo ISÓSCELES!')
elif r1 != r2 and r1 != r3 and r1 != r3:
    print('É possível formar um triângulo ESCALENO!')


