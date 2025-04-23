def voto(ano):
    from datetime import date
    idade = date.today().year - ano

    if 65 > idade >= 18:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO"
    if 18 > idade >= 16 or idade > 65:
        return f"Com {idade} anos: VOTO OPCIONAL"
    else:
        return f"Com {idade} anos: VOTO NEGADO"


print('-'*20)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
