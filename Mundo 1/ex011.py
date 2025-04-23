alt = float(input('Qual a altura da parede em metros? '))
lar = float(input('Qual a largura da parede em metros? '))
area = alt * lar
print('A área da parede é {:.2f}m, são necessários {:.2f} litros de tinta para pintar'.format(area, area/2))
