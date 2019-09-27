while True:
    num = int(input('Deseja ver a tabuada de qual valor?: '))
    if num < 0:
        break
    print('-'*30)
    for cont in range(1,11):
        valor = num * cont
        print(f'{num} x {cont} = {valor}')
    print('-' * 30)
print('Programa de tabuada encerrado! Volte sempre.')