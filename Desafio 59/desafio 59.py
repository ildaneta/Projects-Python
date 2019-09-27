num1 = int(input('Digite o 1º valor: '))
num2 = int(input('Digite o 2º valor: '))
opc = 0
while not opc == 5:
    print('--' * 10)
    print("""[ 1 ] Somar
[ 2 ] Multiplicar 
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do programa""")
    print('--' * 10)
    opc = int(input('Digite a opção desejada: '))
    if opc == 1:
        soma = num1 + num2
        print('A soma dos números {} + {} = {}'.format(num1,num2,soma))
    elif opc == 2:
        mult = num1 * num2
        print('A multiplicação dos números {} x {} = {}'.format(num1,num2,mult))
    elif opc == 3:
        if num1 > num2:
            print('O maior número digitado foi o: {}'.format(num1))
        elif num1 == num2:
            print('Os números {} e {} são iguais.'.format(num1,num2))
        elif num2 > num1:
           print('O maior número digitado foi o: {}'.format(num2))
    elif opc == 4:
        num1 = int(input('Digite o 1º número novamente: '))
        num2 = int(input('Digite o 2º número novamente: '))
print('Fim')
