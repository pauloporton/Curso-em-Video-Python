r1 = int(input('Digite o valor do 1° segmento de reta: '))
r2 = int(input('Digite o valor do 2° segmento de reta: '))
r3 = int(input('Digite o valor do 3° segmento de reta: '))
if r1 + r2 <= r3 or r1 + r3 <= r2 or r2 + r3 <= r1:
    print('Não é possível formar um triângulo!')
else:
    print('É possível formar um triângulo!')
