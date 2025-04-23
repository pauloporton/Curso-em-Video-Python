from datetime import date
print('-=-'*11)
print('CONFEDERAÇÃO BRASILEIRA DE NATAÇÃO')
print('-=-'*11)
ano = int(input('Qual o ano de nascimento do atleta? '))
idade = date.today().year - ano
print('-=-'*11)
print('O atleta tem {} anos'.format(idade))
print('Categoria a ser disputada: ', end='')
if idade <= 9:
    print('MIRIM')
elif 9 < idade <= 14:
    print('INFANTIL')
elif 14 < idade <= 19:
    print('JUNIOR')
elif 19 < idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
print('-=-' * 11)


