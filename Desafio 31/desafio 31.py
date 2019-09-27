dist = float(input('Qual a distância em KM de sua viagem? '))
if dist <= 200:
    precviag = dist * 0.5
    print('Sua viagem ficará no valor de R${:.2f}'.format(precviag))
else:
    precviag = dist * 0.45
    print('Sua viagem ficará no valor de R${:.2f}'.format(precviag))