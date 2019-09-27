from random import randint
cont = 0
while True:
    print('--' * 20)
    print('Vamos Jogar PAR ou ÍMPAR')
    print('--' * 20)
    jog = int(input('Diga um valor (de 0 a 10): '))
    escolhajog = str(input('Par ou Ímpar? [P/I] '))
    pc = randint(0,10)
    soma = jog + pc
    if soma % 2 == 0:
        dec = 'P'
        resp = 'DEU PAR'
    else:
        resp = 'DEU IMPAR'
        dec = 'I'
    print('=-' * 30)
    print(f'Você jogou {jog} e o computador jogou {pc}. Total de {soma} {resp}')
    print('=-' * 30)
    if escolhajog == 'P' and dec == 'P':
        cont += 1
        print('Você GANHOU!')
    elif escolhajog == 'I' and dec == 'I':
        cont += 1
        print('Você GANHOU!')
    else:
        print('Você PERDEU!')
        break
print(f'GAME OVER! Você venceu {cont} vezes')

