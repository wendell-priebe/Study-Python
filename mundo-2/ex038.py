#escreva um programa que leia 2 numeros inteiros e compareos, mostrando na tela uma mensagem - o primeiro valor é maior - o segundo valor e maior
# - nao existe valor mior os dois sao iguais
num1 = int(input('Primeiro numero :'))
num2 = int(input('Segundo numero :'))
if num1 == num2:
    print('Nao existe valor maior, os dois são iguais: {}'.format(num1))
elif num1 < num2:
    print('O segundo numero {} é maior\n e o primeiro é {} menor'.format(num2,num1))
else:
    print('O primeiro numero {} é maior\n e o segundo é {} menor'.format(num1,num2))
