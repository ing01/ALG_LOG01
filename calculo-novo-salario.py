# Algoritmo que recebe o salário de um funcionário. Calcule e mostre o novo salário, sabendo-se que este sofreu um aumento de 25%.

salario = float(input('Informe o seu salário:'))
novoSalario = salario + (salario * 25/100)
print('Seu novo salário é:',novoSalario)
