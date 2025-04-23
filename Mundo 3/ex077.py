palavras = ('Paulo', 'Anna', 'Julia', 'Raquel',
            'Samuel', 'Fernanda', 'Esdras', 'Leticia')
for c in palavras:
    print(f'\nNa palavra \033[4m{c.upper()}\033[m temos: ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end='/')
