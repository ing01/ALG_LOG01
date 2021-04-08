##Sabe-se que: pé = 12 polegadas; 1 jarda = 3 pés; 1 milha = 1,760 jarda
##Faça um programa que receba uma medida em pés, faça as conversões a seguir e mostre os resultados.
##Polegadas; Jardas; Milhas.

pes = float(input('Insira uma medida em pés: '))
polegadas = pes*12
jardas = pes/3
milhas = jardas/1760
print('A conversão em outras medidas é de:',polegadas,'polegadas; ')
print(jardas,'jardas e',milhas,'milhas.')
