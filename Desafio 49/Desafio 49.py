n = int(input('Insira o número que deseja saber sua tabuada: '))
print('-'*13)
for cont in range(1,11):
    resul = n * cont
    print('{} x {:2}  = {}'.format(n,cont,resul))
print('-'*13)