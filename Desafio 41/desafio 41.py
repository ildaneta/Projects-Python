from datetime import date
print('=-'*18)
print('  Classificação de Atletas Natação')
print('=-'*18)
print("""-------------------------
Tabela de Classificação
* Até 09 anos: Mirim
* Até 14 anos: Infantil
* Até 19 anos: Júnior
* Até 20 anos: Sênior
* Acima: Master
-------------------------""")
ano = int(input('Informe o ano de nascimento: '))
anoatual = date.today().year
if anoatual - ano <= 9:
    idade = anoatual - ano
    print('Atleta tem: {} anos.'.format(idade))
    print('Classificação: MIRIM')
elif anoatual - ano <= 14:
    idade = anoatual - ano
    print('Atleta tem: {} anos.'.format(idade))
    print('Classificação: INFANTIL')
elif anoatual - ano <= 19:
    idade = anoatual - ano
    print('Atleta tem: {}'.format(idade))
    print('Classificação: JÚNIOR')
elif anoatual - ano == 20:
    idade = anoatual - ano
    print('Atleta tem: {} anos.'.format(idade))
    print('Classificação: SÊNIOR')
else:
    idade = anoatual - ano
    print('Atleta tem: {} anos.'.format(idade))
    print('Classificação: MASTER')
