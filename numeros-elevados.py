# Algoritmo que recebe dois números maiores que zero, calcule e mostre um elevado ao outro.

numero1 = float(input('Digite um número maior que zero: '))
numero2 = float(input('Digite outro número maior que zero: '))
numero1_elev2 = numero1**numero2
numero2_elev1 = numero2**numero1
print('O seu primeiro número elevado ao segundo número é igual à',numero1_elev2)
print('O seu segundo número elevado ao primeiro número é igual à',numero2_elev1)
