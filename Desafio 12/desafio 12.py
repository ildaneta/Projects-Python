p = float(input('Informe o preço em R$ do produto:'))
desc = p * 0.05
novp = p - desc
print('O preço do produto R${} com 5% de desconto é: R${}'.format(p,novp))
