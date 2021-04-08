##Faça um programa que receba a medida do ângulo (em graus) formado por uma escada apoiada no chão e encostada na parede e a altura da parede onde está a ponta da escada. 
##Calcule e mostre a medida dessa escada.

angulo = int(input('Qual o ângulo da escada? '))
altura = float(input('Qual a altura da escada? '))
radiano = angulo * 3.14/180
import math
escada = altura /math.sin(radiano)
print('Essa é a medida da escada:',escada)
