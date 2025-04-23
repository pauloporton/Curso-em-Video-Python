print('{:=^40}'.format(' LOJAS PORTO '))
p1 = float(input('Qual o valor total das compras? '))
print('-=-' * 15)
print('''FORMAS DE PAGAMENTO: 
[ 1 ] à vista dinheiro/pix
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
pagamento = int(input('Qual a forma de pagamento? '))
print('-=-' * 15)
if pagamento == 1:
    print('Suas compras de R${:.2f} sairão por: R${:.2f}'.format(p1, p1 * 0.9))
elif pagamento == 2:
    print('Suas compras de R${:.2f} sairão por: R${:.2f}'.format(p1, p1 * 0.95))
elif pagamento == 3:
    print('Serão pagas 2x parcelas de R${:.2f}'.format(p1/2))
    print('Suas compras sairão por: R${:.2f}'.format(p1))
elif pagamento == 4:
    print('Suas compras de R${} sairão por: R${:.2f}'.format(p1, p1 * 1.2))
else:
    print('Forma de pagamento inválida.')

