from datetime import date
totmaior = 0
totmenor = 0
for c in range(0,5):
    nasc = int(input('Digite o ano do seu nascimento: '))
    idade = date.today().year - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('{} pessoas são maiores de idade.'.format(totmaior))
print('{} pessoas são menores de idade'.format(totmenor))


