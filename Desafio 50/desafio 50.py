print('=-'*10)
print('   Soma dos pares')
print('=-'*10)
soma = 0
for cont in range(1,7):
    num = int(input('Digite o {}º número: '.format(cont)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('A soma dos números pares digitados é: {}'.format(soma))
