# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
cel = float(input('Qual a temperatura em \033[34mºC \033[m:'))
far = (cel * 9/5) + 32
print('A temperatura \033[34m{:.1f}Cº\033[m corresponde a \033[36m{:.1f}Fº\033[m'.format(cel,far))

