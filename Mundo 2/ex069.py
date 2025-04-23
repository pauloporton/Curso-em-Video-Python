totmaior = 0
totM = 0
totF20 = 0
while True:
    print('-=-'*10)
    print('     CADASTRE UMA PESSOA')
    print('-=-'*10)
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('SEXO (M/F): ').upper().strip()[0]
    print('-=-'*10)
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? (S/N) ').upper().strip()
    if idade >= 18:
        totmaior += 1
    if sexo == 'M':
        totM += 1
    elif sexo == 'F':
        if idade < 20:
            totF20 += 1
    if resp == 'N':
        break
print('-=-'*10)
print(f'FORAM CADASTRADOS: \n{totmaior} pessoas com mais de 18 anos. \n{totM} homens. \n{totF20} mulheres com menos de 20 anos.')


