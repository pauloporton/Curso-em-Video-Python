times = ('BOTAFOGO', 'PALMEIRAS', 'FLAMENGO', 'FORTALEZA', 'INTERNACIONAL','SÃO PAULO',
        'CORINTHIANS', 'BAHIA', 'CRUZEIRO', 'VASCO', 'VITÓRIA', 'ATLÉTICO MG',
         'FLUMINENSE', 'GRÊMIO', 'JUVENTUDE', 'RB BRAGANTINO', 'ATHLETICO PR', 'CRICIÚMA',
         'ATLÉTICO GO', 'CUIABÁ')
print('-=-'*20)
print(f'Times brasileirão 2024: {times}')
print('-=-'*20)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=-'*20)
print(f'Os rebaixados são: {times[16:]}')
print('-=-'*20)
print(f'Ordem alfabética: {sorted(times)}')
print('-=-'*20)
print(f'FLAMENGO está na {times.index('FLAMENGO') + 1}ª posição.')
