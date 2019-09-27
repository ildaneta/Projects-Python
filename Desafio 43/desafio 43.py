print('=-'*15)
print('      Calculando o IMC')
print('=-'*15)
alt = float(input('Digite a altura em metros: '))
peso = float(input('Digite seu peso: '))
imc = peso / (alt*alt)
if imc < 18.5:
    print('O IMC está com o valor de {:.2f} abaixo de 18.5'.format(imc))
    print('Resultado: ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print('O IMC está com o valor de {:.2f} entre 18.5 e 25'.format(imc))
    print('Resultado: PESO IDEAL')
elif imc >= 25 and imc < 30:
    print('O IMC está com o valor de {:.2f} entre 25 e 30'.format(imc))
    print('Resultado: SOBREPESO')
elif imc >= 30 and imc < 40:
    print('O IMC está com o valor de {:.2f} entre 30 e 40'.format(imc))
    print('Resultado: OBESIDADE')
elif imc > 40:
    print('O IMC está com o valor de {:.2f} acima de 40'.format(imc))
    print('Resultado: OBESIDADE MÓRBITA')