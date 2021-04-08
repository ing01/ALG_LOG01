##Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre: a idade dessa pessoa; quantos anos ela terá em 2050.

nome = input('Digite o seu nome: ')
ano_nasc = int(input('Digite o seu ano de nascimento: '))
ano_atual = 2020
idade_atual = ano_atual - ano_nasc
idade2050 = 2050-ano_nasc
print('Sua idade atual é de',idade_atual,'anos!')
print('Você terá',idade2050,'anos em 2050!')
