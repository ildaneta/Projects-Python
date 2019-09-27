print('=-'*12)
print(' Progressão Aritmética')
print('=-'*12)
primtermo = int(input('Informe o 1º termo da sua P.A.: '))
razao = int(input('Informe a razão: '))
num = primtermo
# O for irá repetir o cálculo 10x
for cont in range(1,11):
    calc = num + razao
    print(num,' -> ',end=' ')
    num = calc
print('Acabou')