print('--'*10)
print('LOJA DA ILDA')
print('--'*10)
maior1000 = 0
soma = 0
cont = 0
menorval = 0
while True:
    nomeprod = str(input('Nome do produto: '))
    while not nomeprod:
        nomeprod = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    while not preco:
        preco = float(input('Preço: R$'))
    if preco > 1000:
        maior1000 += 1
    soma = preco + soma
    resp = str(input('Deseja continuar? [S/N]: ')).upper()
    while resp not in 'SN' or not resp:
        resp = str(input('Deseja continuar? [S/N]: ')).upper()
    cont += 1
    if cont == 1:
        menorval = preco
        nomeprodbarato = nomeprod
    if preco < menorval:
        nomeprodbarato = nomeprod
        menorval = preco
    if resp == 'N':
        break
print(f'O total gasto em compras foi de : R${soma:.2f}')
print(f'O total de produtos que custaram mais de R$1000.00 foi {maior1000} produtos.')
print(f'O produto mais barato foi: {nomeprodbarato} que custou R${menorval:.2f}')