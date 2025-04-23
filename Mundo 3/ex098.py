from time import sleep
def contador(inicio, fim, passo):
    print('-=' * 15)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if passo == 0:
       passo = 1

    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            print(f'{c}', end=' ')
            sleep(0.3)
        print('FIM!')
    if inicio > fim:
        for c in range(inicio, fim - 1, -abs(passo)):
            print(f'{c}', end=' ')
            sleep(0.3)
        print('FIM!')
    print('-='*15)


contador(1, 10, 1)
print()
contador(10, 0, 2)
print()
i = int(input('Digite o início da contagem: '))
f = int(input('Digite o fim da contagem: '))
p = int(input('Digite o passo: '))
contador(i, f, p)
