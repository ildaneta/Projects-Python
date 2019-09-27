print('=-'*12)
print(' Progressão Aritmética')
print('=-'*12)
primtermo = int(input('Informe o 1º termo da sua P.A.: '))
razao = int(input('Informe a razão: '))
num = primtermo
cont = 0
while cont < 10:
    calc = num + razao
    print(num,' -> ',end=' ')
    num = calc
    cont = cont + 1
print('Acabou')