#escreva um programa que pergunte o salario de um funcionario e calcule o valor de seu aumento
#para salarios superiores a r$1250.00 calcule um aumento de 10%
#para inferiores ou igual, o aumento é de 15%
sal = float(input('Qual o salario atual do funcionario? R$'))
if sal <=1250:
    print('Seu novo salario é R${:.2f}'.format(sal+((sal*15)/100)))
else:
    print('Seu novo salario é R${:.2f}'.format(sal+((sal*10)/100)))
