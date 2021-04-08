##Pedro comprou um saco de ração com peso em quilos. Ele possui dois gatos, para os quais fornece a quantidade de ração em gramas. 
##A quantidade diária de ração fornecida para cada gato é sempre a mesma.  Faça um programa que receba o peso do saco de ração em gramas e
##a quantidade de ração fornecida para cada gato, calcule e mostre quanto restará de ração no saco após cinco dias.

peso = float(input('Quantos kg tem o saco de ração? '))
racao1 = float(input('Quantos gramas o primeiro gato come? '))
racao2 = float(input('Quantos gramas o segundo gato come? '))
total = peso - 5*(racao1+racao2)
print('No saco de ração restará',total,'kg após 5 dias de alimentação.')
