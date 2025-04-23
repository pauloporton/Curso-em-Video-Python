v = float(input('Qual a velocidade do carro em km/h? '))
if v > 80:
    print('Você foi multado em: R${:.2f}'.format((v-80)*7))
else:
    print('Ok! Boa viagem!')
