masc = 0
maiorid = 0
mulhermen20 = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [F/M]: ')).upper()
    while sexo not in 'FM' or not sexo:
        sexo = str(input('Digite o sexo [F/M]: '))
    resp = str(input('Você deseja continuar? [S/N]: ')).upper()
    while resp not in 'SN' or not resp:
            resp = str(input('Você deseja continuar? [S/N]: ')).upper()
    if sexo == 'M':
        masc += 1
    if idade >= 18:
        maiorid += 1
    if sexo == 'F' and idade < 20:
        mulhermen20 += 1
    if resp == 'N':
        break
print(f'A quantidade de pessoas maiores de 18 anos foi: {maiorid}')
print(f'A quantidade de homens cadastros foi: {masc}')
print(f'A quantidade de mulheres que possuem menos de 20 anos foi: {mulhermen20}')