from time import sleep
print('=-'*11)
print(' Contagem Regressiva')
print('=-'*11)
print('Os fogos irão estourar em...')
for cont in range(10,-1,-1):
    print(cont)
    sleep(1)
print('Boom! Boom! POOOW!')