totidade = 0
velho = 0
tot20 = 0
nomevelho = ''
for c in range(1,5):
    print('---- {}° PESSOA ----'.format(c))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo (F/M): ').strip().lower()
    totidade = totidade + idade
    if sexo == 'm':
        if idade > velho:
            velho = idade
            nomevelho = nome
    elif sexo == 'f':
        if idade < 20:
            tot20 = tot20 + 1
media = totidade / 4
print()
print('A média de idade do grupo é: {:.1f} anos'.format(media))
print('O homem mais velho é: {}'.format(nomevelho))
print('A quantidade de mulheres com menos de 20 anos é: {}'.format(tot20))


