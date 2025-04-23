print('---' * 10)
print('   SEQUÊNCIA DE FIBONACCI')
print('---' * 10)
n = int(input('Quantos termos você quer mostrar? '))
print('-=-' * 10)
c = 1
termoAtual = 0
termoAnterior = 0
proximoTermo = 1
while c < n+1:
    print(termoAtual, end=' -> ')
    termoAnterior = termoAtual
    termoAtual = proximoTermo
    proximoTermo += termoAnterior
    c += 1
print('FIM')
print('-=-' * 10)

