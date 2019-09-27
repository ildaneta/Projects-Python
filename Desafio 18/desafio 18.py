#Informar o angulo e o sistema calcular o seno, tangente, cosseno
#Tem que transformar o angulo em radiano para que o seno, cosseno e tangente possam ser calulados
import math
ang = float(input('Digite o ângulo que você deseja: '))
cos = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang,sen))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang,sen))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang,tan))