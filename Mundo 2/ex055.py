menor = 0
maior = 0
for c in range(1,6):
    peso = float(input('Digite o peso(kg) da {}° pessoa: '.format(c)))
    if peso > maior:
        maior = peso
    elif menor == 0 or peso < menor:
        menor = peso
print('A pessoa MAIS PESADA pesa: {} kg'.format(maior))
print('A pessoa MAIS LEVE pesa: {} kg'.format(menor))




