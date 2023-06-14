# Algoritmo que recebe um número real, encontra e mostra: a parte inteira desse número; a parte fracionária desse número; o arredondamento desse número.

numero = float(input('Escreva um número real: '))
parte_int = numero // 1
parte_frac = numero - parte_int
numero_arred = round(numero)
print('A parte inteira do seu número é',parte_int)
print('A parte fracionária do seu número é',parte_frac)
print('O arredondamento do seu número é',numero_arred)
