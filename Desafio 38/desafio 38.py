print('=-'*15)
print('      Comparando números')
print('=-'*15)
num1 = int(input('Digite o 1º valor: '))
num2 = int(input('Digite o 2º valor: '))
if num1 > num2:
    print('O número {} é maior que o número {}'.format(num1,num2))
elif num2 > num1:
    print('O número {} é maior que o número {}'.format(num2,num1))
else:
    print('Não existe valor maior pois {} e {} são iguais'.format(num1,num2))