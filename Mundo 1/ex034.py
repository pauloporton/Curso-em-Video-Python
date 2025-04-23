sal = float(input('Digite o salário do funcionário: '))
if sal <= 1250.00:
    nsal = sal * 1.15
else:
    nsal = sal * 1.1
print('O novo salário do funcionário será de: R${:.2f}'.format(nsal))