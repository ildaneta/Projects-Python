print('=-'*12)
print(' Progressão Aritmética')
print('=-'*12)
primtermo = int(input('Informe o 1º termo da sua P.A.: '))
razao = int(input('Informe a razão: '))
num = primtermo
cont = 0
total = 0
opc = 10
while opc != 0:
    total = total + opc
    while cont <= total:
        calc = num + razao
        print(num,' -> ',end=' ')
        num = calc
        cont = cont + 1
    print('Pausa')
    opc = int(input('Quantos termos você deseja mostrar a mais?: '))
print('Fim')




