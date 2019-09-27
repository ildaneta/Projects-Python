print('=-'*10)
print(' Número PRIMO')
print('=-'*10)
num = int(input('Digite um número inteiro: '))
totdivisieis = 0
for cont in range(1, num+1):
    if num % cont == 0: #Se o número for divísil pelo número que está no contador, ele fica vermelho e o total de divisores ganha +1
        print('\033[31m',end=' ')
        totdivisieis = totdivisieis + 1
    else:#Se não ele fica cinza
        print('\033[37m', end=' ')
    print('{}'.format(cont),end=' ')
if totdivisieis <= 2:
    print('\033[m O número {} é PRIMO'.format(num))
else:
    print('\033[m O número {} NÃO é PRIMO.'.format(num))