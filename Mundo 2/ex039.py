from datetime import date
ano = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano
print('-=-'*10)
if idade < 18:
    print('VOCÊ DEVE SE ALISTAR EM {} ANOS.'.format(18 - idade))
elif idade == 18:
    print('VOCÊ DEVE SE ALISTAR ESSE ANO.')
else:
    print('VOCÊ SE ALISTOU {} ANOS ATRÁS.'.format(idade - 18))
print('-=-'*10)


