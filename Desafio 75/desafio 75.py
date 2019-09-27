num = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print(f'Os números digitados foram: {num}')
qnt9 = num.count(9)
print(f'O número 9 apareceu {qnt9} vezes')
if 3 in num:
    print(f'O primeiro número 3 digitado foi na {num.index(3) + 1}ª posição')
else:
    print('Não houve nenhum valor 3 digitado')
par = 0
if num[0] % 2 == 0:
    par = 1
elif num[1] % 2 == 0:
    par += 1
elif num[2] % 2 == 0:
    par += 1
elif num[3] % 2 == 0:
    par += 1
print(f'Os valores pares digitados foram: {par}')