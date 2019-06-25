print('-------------------')
print('    Desafio 10')
print('-------------------')
print('')
real = float(input('Informe quantos R$ você possui: '))
dolar = float(input('Informe o valor da cotação do dólar hoje: $'))
conv = real / dolar
print('')
print('Com o valor de R${:.2f} você consegue comprar ${:.2f} dólares.'.format(real,conv))
