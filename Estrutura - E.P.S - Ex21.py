##Uma pessoa deseja pregar um quadro em uma parede. Faça um programa para calcular e mostrar a que distância a escada deve estar da parede. 
##A pessoa deve fornecer o tamanho da escada e a altura em que deseja pregar o quadro. Lembre-se de que o tamanho da escada deve ser maior que a altura que se deseja alcançar.

Z = float(input('Qual a altura da escada? '))
X = float(input('Qual a altura que você deseja pregar o quadro? '))
Y = Z**2 - X**2
Y = Y **1/2
print('Essa é a distância que a escada deve estar da parede: ',Y)
