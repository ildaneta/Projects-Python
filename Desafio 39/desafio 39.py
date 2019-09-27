from datetime import date
print('=-'*15)
print('      Alistamento Militar')
print('=-'*15)
anonasc = int(input('Informe o ano do seu nascimento: '))
sexo = input('Informe seu sexo [M/F]: ')
anoatual = (date.today().year)
idade = anoatual - anonasc
if sexo == 'M':
    if (anoatual - anonasc) < 18:
        tempo = 18 - (anoatual - anonasc)
        anoalist = anoatual + tempo
        print('Quem nasceu em {} tem {} anos em {}.'.format(anonasc, idade, anoatual))
        print('Ainda falta(m) {} ano(s) para o alistamento!'.format(tempo))
        print('Seu alistamento será em {}!'.format(anoalist))
    elif (anoatual - anonasc) == 18:
        print('Quem nasceu em {} tem {}{} anos{} em {}.'.format(anonasc,'\033[1;36m',idade,'\033[m', anoatual))
        print('O alistamento deve ser realizado IMEDIATAMENTE. {}Cuidado para não perder o prazo!{}'.format('\033[1;4;33m', '\033[m'))
    elif (anoatual - anonasc) > 18:
        tempo = (anoatual - anonasc) - 18
        anoalist = anoatual - tempo
        print('Quem nasceu em {} tem {} anos em {}.'.format(anonasc, idade, anoatual))
        print('{}Você {}PERDEU{}{} o prazo de alistamento há{} {}{} ano(s){}!'.format('\033[1m','\033[1;4;31m','\033[m','\033[1m','\033[m','\033[1;4;31m',tempo,'\033[m'))
        print('O alistamento deveria ter sido realizado no ano de {}{}{}!'.format('\033[1;4;31m',anoalist,'\033[m'))
else:
    print('Devido ao sexo ser Feminino, o alistamento militar não é obrigatório!')
