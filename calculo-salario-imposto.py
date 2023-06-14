# Algoritmo que recebe o salário base de um funcionário, calcule e mostre o salário a receber, sabendo-se que o funcionário tem gratificação de 5% sobre o
# salário base e paga imposto de 7% também sobre o salário base.

salario_base = float(input('Informe o salário base do funcionário: '))
gratificacao = salario_base * 5/100
imposto = salario_base * 7/100
salario_recebe = salario_base + gratificacao - imposto
print('O salário que o funcionário deve receber é de R$',salario_recebe)
