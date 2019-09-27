sexo = input('Informe o sexo [F/M]: ').strip().upper()[0]
while sexo not in 'FM':
    sexo = input('Dados inválidos. Por favor, informe o sexo [F/M]: ').strip().upper()[0]
print('O sexo {} foi digitado corretamente.'.format(sexo))
