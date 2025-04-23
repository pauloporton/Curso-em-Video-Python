lista = []
pessoa = {}
tot = 0
somaidades = 0
while True:
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo: (M/F) ').strip().upper()
    pessoa['idade'] = int(input('Idade: '))
    somaidades += pessoa['idade']
    lista.append(pessoa.copy())
    tot += 1
    while True:
        resp = input('Quer continuar? (S/N) ').strip().upper()
        if resp not in 'SN':
            print('TENTE NOVAMENTE.', end='')
        else:
            break
    if resp == 'N':
        break
media = somaidades/tot
print('-='*20)
print(f'- O grupo tem {tot} pessoas.')
print(f'- A média de idade do grupo é de: {media:.2f}')
print(f'- As mulheres cadastradas foram: ', end='')
for c in lista:
    if c['sexo'] == 'F':
        print(c['nome'], end=' ')
print()
print('- Lista das pessoas que estão acima da média de idade: ')
for v in lista:
    if v['idade'] > media:
        print(v)


