print('==='*10)
print('         BANCO PORTO')
print('==='*10)
valor = int(input('Qual valor você quer sacar? R$'))
notas50 = valor // 50
valor = valor - notas50*50
notas20 = valor // 20
valor = valor - notas20*20
notas10 = valor // 10
valor = valor - notas10*10
notas1 = valor // 1
print('==='*10)
print(f'Total de {notas50} cédulas de R$50 ')
print(f'Total de {notas20} cédulas de R$20')
print(f'Total de {notas10} cédulas de R$10')
print(f'Total de {notas1} cédulas de R$1')
print('==='*10)
print('VOLTE SEMPRE AO BANCO PORTO! Tenha um bom dia.')
