# Algoritmo que recebe o salário de um funcionário e o percentual de aumento, calcule e mostre o valor do aumento e o novo salário.

salario = float(input('Informe o seu salário:'))
percentual = float(input('Informe o percentual de aumento do seu salário:'))
aumento = salario * percentual/100
print('Seu aumento será de R$',aumento)
novo_salario = salario + aumento
print('Seu novo salário será R$', novo_salario)
