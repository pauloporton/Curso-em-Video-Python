def leiaint(num):
    while True:
        try:
            valor = int(input(num))
        except (TypeError, ValueError):
            print('\033[0;31mERRO. Digite um valor inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return valor


def leiafloat(num):
    while True:
        try:
            valor = float(input(num))
        except(TypeError, ValueError):
            print('\033[0;31mERRO. Digite um valor real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return valor


n1 = leiaint('Digite um número inteiro: ')
n2 = leiafloat('Digite um número real: ')
print(f'\033[0;32mVocê digitou o número inteiro {n1} e o número real {n2} \033[m')
