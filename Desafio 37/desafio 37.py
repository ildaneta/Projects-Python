print('=-'*15)
print('     Conversão de bases numéricas')
print('=-'*15)
num = int(input('Digite um número inteiro: '))
print("""Escolha qual das opções abaixo deseja converter:
      [1] Binário
      [2] Octal
      [3] Hexadecimal
      """)
opc = int(input('Sua opção: '))
if opc == 1:
    print(bin(num)[2:]) #O [2:] delimita a exibir o texto a partir da 3º casa em diante
elif opc == 2:
    print(oct(num)[2:])
elif opc == 3:
    print(hex(num)[2:])
else:
    print('Opção inválida.')