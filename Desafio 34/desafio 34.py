sal = float(input('Digite o valor do seu salário: R$'))
if sal <= 1250:
    novsal = sal + (sal * 0.15)
    print('O seu salário de R${:.2f} sofreu um aumento de 15% seu novo salário é: R${:.2f}'.format(sal,novsal))
else:
    novsal = sal + (sal * 0.10)
    print('O seu salário de R${:.2f} sofreu um aumento de 10% seu novo salário é: R${:.2f}'.format(sal,novsal))