def leiaDinheiro(msg):
      valido = False
      while not valido:
        entrada = input(msg).replace(',', '.' ).strip()
        if entrada.isalpha() or entrada == '':
            print('\033[0;31mERRO. Digite um preço válido.\033[m')
        else:
            valido = True
            return float(entrada)


