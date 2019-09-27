print('=-'*12)
print('Soma dos ímpares múltiplos de 3')
print('=-'*12)
soma = 0
for cont in range(1,501,2):
    if cont % 3 == 0:
        print(cont, end=' ')
        soma = soma + cont
print('A soma de todos os valores múltiplos de 3 é {}'.format(soma, end=' '))