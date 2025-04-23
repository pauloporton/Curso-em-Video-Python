lista = []
aluno = []
nota = [0, 0]
while True:
    nome = input('Nome: ')
    aluno.append(nome)
    nota1 = float(input('Nota 1: '))
    nota[0] = nota1
    nota2 = float(input('Nota 2: '))
    nota[1] = nota2
    aluno.append(nota[:])
    media = (nota1 + nota2) / 2
    aluno.append(media)
    lista.append(aluno[:])
    aluno.clear()
    while True:
        resp = input('Quer continuar? (S/N) ').strip().upper()
        if resp not in 'SN':
            print('TENTE NOVAMENTE. ', end='')
        else:
            break
    if resp == 'N':
        break
print('-=-'*15)
print('N°   NOME           MÉDIA')
print('-'*30)
for c in range(0, len(lista)):
    print(f'{c:<3} | {lista[c][0]:<12} | {lista[c][2]}')
print('-'*30)
while True:
    dados = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if dados == 999:
        break
    else:
        print(f'Notas de {lista[dados][0]}: {lista[dados][1]}')
        print('-'*30)
print('FINALIZANDO...')
print('Volte sempre!')


