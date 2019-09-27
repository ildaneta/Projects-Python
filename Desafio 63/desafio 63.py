print("""--------------------------
  Sequência de Fibonacci
--------------------------""")
num = int(input('Quantos termos você quer mostrar? '))
cont = 0
num1 = 0
num2 = 1
print(num1,'->',num2, '-> ',end='')

# O número digitado pelo usuário terá 3 termos retirados pois estes já são exibidos de início
num = num - 3

while cont <= num:
    soma = num1 + num2
    num1 = num2
    num2 = soma
    print('{} -> '.format(soma),end='')
    cont += 1
print('Fim')
