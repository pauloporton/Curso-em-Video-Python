n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
media = (n1 + n2 + n3) / 3
print('-=-' * 10)
print('A média do(a) aluno(a) foi: {:.1f}'.format(media))

if media >= 7:
    print('APROVADO')
elif 5 <= media <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('REPROVADO')
print('-=-' * 10)





