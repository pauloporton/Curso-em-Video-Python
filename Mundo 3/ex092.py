from datetime import date
funcionario = {}
funcionario["Nome"] = input('Nome: ')
anoNasc = int(input('Ano de nascimento: '))
funcionario["Idade"] = date.today().year - anoNasc
funcionario["CTPS"] = int(input('Carteira de trabalho: (0 não tem) '))
if funcionario["CTPS"] != 0:
    funcionario["Contratação"] = int(input('Ano de contratação: '))
    funcionario["Salário"] = float(input('Salário: R$'))
    funcionario["Aposentadoria"] = (funcionario["Contratação"] + 35) - anoNasc
print("-=-"*20)
for k, v in funcionario.items():
    print(f'{k} tem o valor: {v}')

    

