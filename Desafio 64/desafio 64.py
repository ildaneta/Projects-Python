num = 0
cont = 0
soma = 0
num = int(input('Digite um número: '))
while num != 999:
    cont = cont + 1
    soma = soma + num
    num = int(input('Digite um número: '))
print('A quantidade de números digitados foram: {} e soma deles é igual a {}'.format(cont,soma))