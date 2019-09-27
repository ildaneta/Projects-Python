sal = float(input('Informe seu salário: R$'))
aum = sal * 0.15
novsal = sal + aum
print('O salário informado R${} com o aumento de 15% passa a ser: R${:}'.format(sal,novsal))
