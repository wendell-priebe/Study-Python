#faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angu
import math
ang = float(input('Digite o angulo que voce deseja:'))
cos = math.cos(math.radians(ang))
seno = math.sin(math.radians(ang))
tang = math.tan(math.radians(ang))
print('O angulo de {} tem o SENO de {:.2f}'.format(ang, seno))
print('O angolo de {} tem o COSSENO de {:.2f}'.format(ang, cos))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(ang, tang))
  #math.radians converte o valor para angulo em graus
