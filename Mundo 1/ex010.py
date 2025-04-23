reais = float(input('Quantos reais você tem? '))
dolar = reais / 3.27
print('Com R${} você receberá ${:.2f}'.format(reais, dolar))