#faça um programa que leia o comprimento do cateto opsto e do cateto adjacente de um triangulo,
#calcule e mostre o comprimeno da hipotenisa
import math
oposto = float(input('Qual o comprimento do cateto oposto:'))
adjacente = float(input('Qual o comprimento do cateto adjacente:'))
#hipotenusa = (oposto ** 2 + adjacente ** 2 ) ** (1/2)
#print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
hipotenusa = math.hypot(oposto, adjacente)
print(' a hipotenusa vai medir {:.2f}'.format(hipotenusa))
