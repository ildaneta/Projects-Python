from random import randint
cont = 0
computador = randint(0, 10)# faz o computador gerar um número de 0 a 5
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('Em que número eu pensei?.. ')
acertou = False
while not acertou:
    cont = cont + 1
    jogador = int(input('Qual é seu palpite?: '))
    if jogador == computador:
        acertou = True
print('Acertou em {} tentativas. Parabéns!'.format(cont))