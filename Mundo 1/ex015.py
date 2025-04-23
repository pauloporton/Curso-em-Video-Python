d = int(input('Quantos dias você ficou com o carro? '))
km = int(input('Quantos km você rodou com ele? '))
valor = (d * 60) + (km  * 0.15)
print('Você deve pagar R${:.2f}'.format(valor))
