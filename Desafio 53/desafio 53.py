# O programa tem que identificar se a palavra escrita é um palíndromo: palavra que lida de trás pra frente tem o mesmo significado
#o Slipt está particionando a frase
frase = str(input('Digite a frase que deseja analisar: ')).split()
#o Join está rejuntando a frase sem espaços
junto = ''.join(frase).upper()
inverso =''
for letra in range(len(junto) -1, -1, -1):# o código vai começar no comprimento da frase e vai ler do fim pro começo até a primeira palavra
    inverso = inverso + junto[letra]
if inverso == junto:
    print('A palavra {} é palíndroma, pois escrita de trás pra frente fica {}'.format(junto, inverso))
else:
    print('A frase digitada não é palíndroma')