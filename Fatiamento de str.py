frase = 'Curso em Vídeo Python'

#calcula o tamanho da string
print(len(frase))

#O programa conta quantas vezes o 'o' minúsculo aparece da posição 0 até a 12
print(frase.count('o',0,14))

#A partir de que posição ele encontrou o 'deo'
print(frase.find('deo'))

#Quando se recebe o valor -1 quer dizer que não existe na str
print(frase.find('android'))

#O 'in' é utilizado para retornar True ou False
print('Curso' in frase)

##Transformação

#Transformação, quando utilizamos o replace ele troca a primeira str pela segunda
frase.replace('Python','Android')

#transforma todas as str em maiúsculas
frase.upper()

#transforma todas as str em minúsculas
frase.lower()

#transforma todas as str em minúsculas e apenas a primeira letra ficará maiúscula
frase.capitalize()

#transforma todas as str em minúsculas e apenas as primeiras letras de cada palavra ficará maiúscula
# Curso Em Vídeo Python
frase.title()

#Remove todos os espaços do começo da str e os espaços do fim
frase.strip()

#Remove apenas os espaços da direita Right
frase.rstrip()

#Remove apenas os espaços da esquerda Left
frase.lstrip()

##Divisão

#Divide uma str em uma lista separando cada palavra em uma nova cadeia
frase.slipt()

#Juntar o split acima
' '.join(frase)

# colocar """ 3 aspas duplas para escrever um texto completo em um print só
