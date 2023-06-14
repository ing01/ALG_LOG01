# Algoritmo que recebe o valor de um depósito e o valor da taxa de juros, calcule e mostre o valor do rendimento e o valor total depois do rendimento de um mês.

dep = float(input('Digite o valor do depósito: '))
taxa = (input('Digite o valor da taxa de juros: '))
rendimento = dep * taxa/100
total = dep+rendimento
print('O valor do rendimento é igual a R$',rendimento)
print('O valor total do depósito é igual a R$',total)
