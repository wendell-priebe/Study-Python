#faça um algoritimo que leia o salario do funcionario e mostre seu novo salario com 15% de almento
salario = float(input('\033[30mValor do salario atual: R$'))
porcento = float(input('Qual a porcentagem de almento: %'))
futuro = float(input('Valor de salario que deseja receber futuramente: R$'))
aumento = salario * porcento /100
valor = salario + aumento
salfut = futuro - valor
print('Seu antigo salario de R${:.2f} teve um aumento\nSeu novo salario é de R${:.2f}'.format(salario,valor))
print('Com o seu salario com aumento de {}% ainda falta {} para ter o salario que deseja.'.format(porcento,salfut))