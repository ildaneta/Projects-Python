from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 se desejar analisar o ano atual: '))
if ano ==  0:
    ano = date.today().year # Pega-se o ano da máquina do usuário
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))