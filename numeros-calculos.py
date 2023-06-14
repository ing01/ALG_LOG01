# Algoritmo que recebe um número positivo e maior que zero, calcule e mostre: 
# o número digitado ao quadrado; o número digitado ao cubo; araiz do número digitado e a raiz cúbica do número digitado

numero = float(input('Digite um número positivo e maior que zero: '))
quad = numero**2
cubo = numero**3
raiz_quad = numero**0.5
raiz_cub = numero**0.33
print('O seu número ao quadrado é igual à',quad)
print('O seu número ao cubo é igual à',cubo)
print('A raiz quadrada do seu número é igual à',raiz_quad)
print('A raiz cúbica do seu número é igual à',raiz_cub)
