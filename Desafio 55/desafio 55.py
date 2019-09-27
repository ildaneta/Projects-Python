print('=-'*12)
print('   Maior e Menor peso')
print('=-'*12)
maior = 0
menor = 0
for cont in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa em KG: '.format(cont)))
    if cont == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O maior peso digitado foi: {}'.format(maior))
print('O menor peso digitado foi: {}'.format(menor))