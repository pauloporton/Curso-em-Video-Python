# dados do comprador
valor = float(input('Qual o valor da casa? '))
sal = float(input('Qual o seu salário? '))
tempo = int(input('Em quantos anos pretende pagar? '))

# prestação mensal
pm = valor / (tempo*12)
if pm <= sal * 0.3:
    print('O valor da prestação mensal durante os {} anos será de: R${:.2f}'.format(tempo, pm))
else:
    print('Desculpa, não poderemos fechar esse negócio. ')
