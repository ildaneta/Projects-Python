# Fazer a média de idade, o homem mais velho e quantas mulheres tem menos de 20 anos.
print('=-'*12)
print(' Analisador de Pessoas')
print('=-'*12)
print('')
media = 0
totidade = 0
maioridade = 0
menosde20 = 0
for cont in range(1,5):
    print('------ {}ª PESSOA ------'.format(cont))
    nome = input('Nome: '.format(cont))
    idade = int(input('Idade: '.format(cont)))
    sexo = input('Sexo [M/F]: '.format(cont))
    totidade = totidade + idade
    media = totidade / cont
    if cont == 1:
        maioridade = idade
    if sexo in 'M m' and idade > maioridade:
        nomevelho = nome
        maioridade = idade
    if sexo in 'F f' and idade < 20:
        menosde20 = menosde20 + 1
print('-----------------------')
print('A média das idades informadas é: {} anos'.format(media))
print('O homem mais velho foi: {} com {} anos.'.format(nomevelho,maioridade))
print('A quantidade de mulheres com idade inferior a 20 anos foi: {} pessoas.'.format(menosde20))