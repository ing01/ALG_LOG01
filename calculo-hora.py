# Algoritmo que recebe uma hora formada por hora e minutos (um número real), calcule e mostre a hora digitada apenas em minutos. 
# Lembre-se de que: para quatro e meia, deve-se digitar 4.30; os minutos vão de 0 a 59

hora = float(input('Que horas são? '))
h = hora // 1
minutos = hora - h
conversao = (h*60) + (minutos * 100)
print('Seu horário é',conversao,'em minutos.')
