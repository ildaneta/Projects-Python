from datetime import date
print('=-'*12)
print('  Grupo da Maioridade')
print('=-'*12)
anoatual = date.today().year
totmaior = 0
totmenor = 0
for cont in range(1,8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa:'.format(cont)))
    if anoatual - ano >= 18:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor + 1
print('O total de pessoas maiores de idade foi: {}'. format(totmaior))
print('O total de pessoas menores de idade foi: {}'.format(totmenor))