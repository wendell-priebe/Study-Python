#faça um programa que mostre na tela um contagem regressiva para o estouro de fogos de artificio, indo de 10 a 0 com pausa de 1 seg entre eles
from time import sleep
import emoji
for c in range (10, 0, -1):
    print(c)
    sleep(1)
print(emoji.emojize(':v:'*10,use_aliases=True))
print('PARABENS !!!')
