print('-='*16)
print('    Analisador de Triângulos')
print('-='*16)
ladoa = float(input('Digite o valor do 1º lado: '))
ladob = float(input('Digite o valor do 2º lado: '))
ladoc = float(input('Digite o valor do 3º lado: '))
if ladoa < ladob + ladoc and ladob < ladoa + ladoc and ladoc < ladoa + ladob:
    print('As medidas informadas PODEM FORMAR um triângulo')
    if ladoa == ladob == ladoc:
        print('O triângulo formado é do tipo: EQUILÁTERO.')
    elif ladoa == ladob != ladoc or ladoa == ladoc != ladob or ladoc == ladob != ladoa:
        print('O triângulo formado é do tipo: Isóceles.')
    elif ladoa != ladob !=ladoc:
        print('O triângulo formado é do tipo: Escaleno')
else:
    print('As medidas informadas NÃO PODEM formam um triângulo')