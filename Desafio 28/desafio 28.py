from random import randint
num = randint(0,5) #faz o computador gerar um número de 0 a 5
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
numusu = int(input('Em que número eu pensei?: '))
print('Processando...')
if numusu == num:
    print('Você me venceu!')
else:
    print('Não foi dessa vez, tente novamente!')
