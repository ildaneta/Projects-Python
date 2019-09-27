print('=-'*15)
print('  Gerenciador de Pagamentos')
print('=-'*15)
preco = float(input('Informe o valor do produto: R$'))
print("""Condições de pagamento:
[1] À vista Dinheiro / Cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão""")
pag = int(input('Informe a condição do pagamento: '))
if pag == 1:
    valor = preco - (preco * 0.1)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final. Desconto de 10%'.format(preco,valor))
elif pag == 2:
    valor = preco - (preco * 0.05)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final. Desconto de 5%'.format(preco,valor))
elif pag == 3:
    print('Sua compra de R${:.2f} vai custar o preço normal, sem descontos.'.format(preco))
elif pag == 4:
    valor = preco + (preco * 0.2)
    print('Sua compra de R${:.2f} vai custar R${:.2f} devido a juros de 20%'.format(preco,valor))

