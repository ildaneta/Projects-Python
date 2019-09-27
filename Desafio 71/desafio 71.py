print('=='*20)
print('{:^40}'.format('Banco Do PYTHON'))
print('=='*20)
totalced = total = 0
ced = 50
valor = int(input('Qual valor você deseja sacar? R$'))
total = valor
while True:
   if total >= ced:
       total = total - ced
       totalced += 1
   else:
       if totalced > 0:
           print(f'Total de {totalced} cédulas de R${ced}')
       if ced == 50:
           ced = 20
       elif ced == 20:
           ced = 10
       elif ced == 10:
           ced = 1
       totalced = 0
       if total == 0:
           break
print('=='*20)
print('Volte sempre ao Banco PYTHON! Tenha um bom dia!')


