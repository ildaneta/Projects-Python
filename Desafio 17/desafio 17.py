#Faça um programa que leia o comprimento do cateto adjacente de um triânguo retângulo, calcule e mostre o comprimento da hipotenusa
import math
catop = float(input('Comprimento do cateto oposto: '))
catadj = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa vai medir: {:.2f} '.format(math.hypot(catop,catadj)))

