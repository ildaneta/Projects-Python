listagem = ('Lápis',1.2,'Borracha',0.55,'Caderno', 9.56, 'Mochila', 49.6, 'Livro',34.9, 'Compasso', 9.99, 'Estojo', 25, 'Régua', 1.55)
titulo = 'LISTAGEM DE PREÇOS'
print('--'*20)
print(titulo.center(40))
print('--'*20)
for posi in range(0, len(listagem)):
    if posi % 2 == 0:
        print(f'{listagem[posi]:.<30}',end='')
    else:
        print(f'{listagem[posi]:.>10.2f}')
print('--'*20)