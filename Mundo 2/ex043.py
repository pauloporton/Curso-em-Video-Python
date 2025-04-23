massa = float(input('Digite sua massa corporal(kg): '))
altura = float(input('Digite sua altura(m): '))
imc = massa / (altura ** 2)
print('-=-' * 10)
print('IMC: {:.1f}'.format(imc))
if imc < 18.5:
    print('VOCÊ ESTÁ \033[4mABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('PARABÉNS! VOCÊ ESTÁ NO \033[4mPESO IDEAL')
elif 25 <= imc < 30:
    print('VOCÊ ESTÁ COM \033[4mSOBREPESO')
elif 30 <= imc < 40:
    print('VOCÊ ESTÁ COM \033[4mOBESIDADE')
else:
    print('VOCÊ ESTÁ COM \033[4mOBESIDADE MÓRBIDA')
print('-=-' * 10)