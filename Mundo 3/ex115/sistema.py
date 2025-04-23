from ex115.lib.interface import *
from time import sleep
from ex115.lib.arquivo import *

arq = ('cursoemvideo.txt')

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do sistema'])
    sleep(0.5)
    if resp == 1:
        # opção de listar um conteúdo de um arquivo
        lerArquivo(arq)
    elif resp == 2:
        # opção de cadastrar uma pessoa
        cabeçalho('NOVO CADASTRO')
        nome = input('Nome: ').strip()
        if nome == '':
            nome = 'desconhecido'
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)

    elif resp == 3:
        # opção de sair do sistema
        cabeçalho('Saindo do sistema...')
        break
    else:
        print('\033[0;31mERRO. Digite uma opção válida.\033[m ')
    sleep(2)

