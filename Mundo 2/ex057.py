sexo = input('Informe o seu sexo: (M/F) ').upper().strip()
while sexo not in 'MmFf':
    sexo = input('DADOS INVÁLIDOS! Por favor, informe seu sexo: (M/F) ').upper().strip()
print('sexo {} registrado com sucesso.'.format(sexo))

