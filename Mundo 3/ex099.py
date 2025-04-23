def maior(*num):
    mai = 0
    print('Analisando os valores passados...')
    print(f'{num} foram informados {len(num)} valores')
    for c in range(0, len(num)):
        if c == 0:
            mai = num[c]

        if num[c] > mai:
            mai = num[c]
    print(f'O maior valor informado foi {mai}')
    print('-=' * 20)


maior(5, 8, 7, 14, 5, 9)
maior(4, 6, 1, 2)
maior(9, 2)
maior(3, 3, 4)

