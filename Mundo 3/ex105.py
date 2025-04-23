def notas(*num, sit=False):
    """
    => Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas de alunos (aceita várias).
    :param sit: valor opcional indicando se deve ou não adicionar situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """

    resultado = dict()
    resultado['total'] = len(num)
    soma = 0
    mai = 0
    men = 0
    for c in range(0, len(num)):
        soma += num[c]
        if c == 0:
           men = num[c]
        if num[c] > mai:
            mai = num[c]
        if num[c] < men:
            men = num[c]
    resultado['maior'] = mai
    resultado['menor'] = men
    media = soma / len(num)
    resultado['média'] = f'{media:.1f}'
    if sit:
        if media >= 7:
            resultado['situação'] = 'BOA'
        if 7 > media > 5.5:
            resultado['situação'] = 'RAZOÁVEL'
        elif media <= 5.5:
            resultado['situação'] = 'RUIM'
    return resultado


resp = notas(4, 5.6, 8, 9, 7.7)
print(resp)