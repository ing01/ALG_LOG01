##Cada degrau de uma escada tem X de altura. Faça um programa que receba essa altura e a altura que o usuário deseja alcançar subindo a escada, calcule e mostre 
##quantos degraus ele deverá subir para atingir seu objetivo, sem se preocupar com a altura do usuário. Todas as medidas fornecidas devem estar em metros.

alturaD = float(input('Quantos metros tem cada degrau? '))
alturaDe = float(input('Qual altura você deseja alcançar subindo a escada? '))
quantD = alturaDe // alturaD
print('Você precisa subir',quantD,'degraus para alcançar seu objetivo.')
