s = 0
cont = 0
while True:
    num = int(input('Digite um número (Use 999 para PARAR): '))
    if num == 999:
        break
    s += num
    cont += 1
print(f'A soma dos {cont} valores digitados é: {s}') #PEP f string