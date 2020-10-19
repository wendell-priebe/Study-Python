# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele
# foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
print('\033[30m Alugel de carros!!\033[m')
dias = int(input('Quantos dias foi alugado :'))
km = float(input('Quantos Km foi rodados :'))
if dias >= 31:
    total = (dias * 58)+(km * 0.12)
    print('O total a pagar é de R${:.2f}'.format(total))
else:
    total = (dias * 60) + (km * 0.15)
    print('O total a pagar é de R${:.2f}'.format(total))