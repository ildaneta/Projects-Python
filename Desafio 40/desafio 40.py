print('=-'*15)
print('       Média do Aluno')
print('=-'*15)
n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
med = (n1+n2)/2
if med < 5:
    print('A média do aluno de {} está abaixo de 7.0 com isso está {}REPROVADO{}!'.format(med,'\033[1;4;30;41m','\033[m'))
elif med >= 5 and med <= 6.9:
    print('A média do aluno de {} está baixo de 7.0 com isso está de {}RECUPERAÇÃO{}!'.format(med,'\033[1;4;30;43m','\033[m'))
elif med > 7:
    print('A média do aluno de {} está compatível com a média da escola. Está {}APROVADO{}!'.format(med,'\033[1;4;30;46m','\033[m'))
