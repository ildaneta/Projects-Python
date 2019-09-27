from random import randint
maiornum = 0
menornum = 0
num = (randint(0,20), randint(0,20), randint(0,20), randint(0,20), randint(0,20))
print('Os valores sorteados foram: ')
for n in num:
    print(f'{n} ', end='')
print(f'\nO menor valor sorteado foi: {max(num)}')
print(f'O maior valor sorteado foi: {min(num)}')

