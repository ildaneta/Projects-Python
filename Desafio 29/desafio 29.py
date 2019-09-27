vel = float(input('Digite a velocidade do carro: '))
if vel > 80:
    multa = (vel - 80) * 7
    print('\033[1;30;41mA velocidade de {:.0f}KM está acima do permitido 80KM!\033[m'.format(vel))
    print ('Você deve pagar uma multa de {}R${:.2f}{}'.format('\033[1;33m',multa,'\033[m'))
else:
    print('Você está dirigindo corretamente!')
print('Tenha um bom dia! Dirija com segurança!')

