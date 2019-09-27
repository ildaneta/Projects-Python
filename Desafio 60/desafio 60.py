print("""-----------
 Fatorial
-----------""")
num = int(input('Digite o número que deseja o fatorial: '))
cont = num
fat = 1
print('Calculando {}! = '.format(num), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ',end='')
    fat = fat * cont
    cont = cont - 1
print('{}'.format(fat))