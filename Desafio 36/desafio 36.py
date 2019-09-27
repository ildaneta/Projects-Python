print('=-'*15)
print('         Empréstimo')
print('=-'*15)
valor = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe o salário do comprador: R$'))
anos = float(input('Quantos anos de financiamento?: '))
minimo = (salario * 30)/100
parcela = (valor / anos) / 12
print('A prestação será de {}R${:.2f}{} por mês durante {}{:.0f}{} anos.'.format('\033[1;33m',parcela,'\033[m','\033[1;31m',anos,'\033[m'))
if parcela > minimo :
    print('O empréstimo foi {}REPROVADO{} devido ao valor da prestação exceder os 30% do salário que é {}R${:.2f}{} '.format('\033[1;30;41m','\033[m','\033[1;30;41m',minimo,'\033[m'))
else:
    print('O empréstimo {}APROVADO{}'.format('\033[1;30;42m','\033[m'))