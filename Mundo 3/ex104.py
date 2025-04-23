def leiaint(num):
    while True:
        valor = input(num)
        if valor.strip().isdigit():
            break
        else:
            print('\033[0;31mERRO. Digite um valor inteiro válido.\033[m')
    return valor


n = leiaint('Digite um número inteiro: ')
print(f'\033[0;32mVocê acabou de digitar o número {n}')