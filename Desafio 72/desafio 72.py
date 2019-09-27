extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito','nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    valor = int(input('Digite um número entre 0 e 20: '))
    while valor not in range(0,21):
        valor = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    for cont in range(0,len(extenso)):
        if valor == cont:
            print(f'Você digitou o número ', extenso[cont])
    break