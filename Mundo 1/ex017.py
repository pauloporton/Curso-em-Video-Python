import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hip = math.hypot(ca, co)
print('A hipotenusa vale: {}'.format(hip))
