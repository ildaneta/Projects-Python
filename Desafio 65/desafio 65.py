resp = 'S'
soma = 0
cont = 0
maior = 0
menor = 0
while resp != 'N':
    num = float(input('Digite um valor: '))
    resp = input('Deseja continuar? [S/N]: ').upper()
    soma = soma + num
    cont = cont + 1
    med = soma / cont
    if cont == 1:
        maior = num
        menor = num
    if cont > 1:
        if num >= maior:
            maior = num
        elif num < menor:
            menor = num
print('Média: {:.2f}, QTD de valores: {}, Maior: {:.1f}, Menor: {:.1f}'.format(med, cont, maior, menor))