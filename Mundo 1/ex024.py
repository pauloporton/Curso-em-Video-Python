city = input('Digite o nome da sua cidade: ')
city = city.lower().split()
print('Essa cidade começa com "Santo" ? {}'.format('santo' in city[0]))