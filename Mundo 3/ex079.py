num = [] #lista onde serão digitados todos os valores
cont = -1 #contador para ter uma referência dos valores
adicionados = [] #lista vazia para receber os valores unitários
while True:
    cont += 1 #o contador recebe 1 a cada loop
    num.append(int(input('Digite um valor: '))) #valor irá para lista "num"
    if num[cont] in adicionados: #analisa se o valor já existe na lista "adicionados"
        print('VALOR DUPLICADO! Não vou adicionar...')
    else:
        adicionados.append((num[cont])) #se for um valor novo, será adicionado
        print('VALOR ADICIONADO!')
    while True: #entrará em loop se a resposta não for S ou N
        resp = input('Quer continuar? (S/N) ').strip().upper()
        if resp not in 'SN':
            print('TENTE NOVAMENTE.', end=' ') #não aceita a resposta
        else:
            break #aceita a resposta se for S ou N
    if resp == 'N':
        break #encerra o loop se responder N
print('-=-' * 20)
adicionados.sort()
print(f'Você digitou os valores: {adicionados}')



