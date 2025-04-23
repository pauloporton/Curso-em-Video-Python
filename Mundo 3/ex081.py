lista = []
resp = ''
while True:
    lista.append(int(input('Digite um valor: ')))
    while True:
        resp = input('Quer continuar? (S/N) ').strip().upper()
        if resp not in 'SN':
            print('RESPOSTA INVÁLIDA.', end="")
        else:
            break
    if resp == 'N':
        break
print('-=-'*10)
print(f'Foram digitados {len(lista)} valores.')
lista.sort(reverse = True)
print(f'Lista na ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')




