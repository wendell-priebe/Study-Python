# elabore um programa que calcule o valor a ser pago por um produto considerando o preço normal e condiçao de pagamento:
#avista/cheque 10% desc ; avista no cartao 5% desc ; ate 2x cartao preço normal ; 3x ou mais 20% de juros
valorprod = float(input('Valor do produto : R$'))
meio = int(input('''Formas de pagamento
 [1] Avista/Cheque
 [2] Avista no cartão
 [3] 2x Parcelado
 [4] 3x ou mais Parcelado
Meio de Pagamento :'''))
if meio == 1:
    print('O valor do produto R${:.2f}, com desconto de 10% é R${:.2f}'.format(valorprod,valorprod-(valorprod*10/100)))
elif meio == 2:
    print('O valor do produto R${:.2f}, com desconto de 5% é R${:.2f}'.format(valorprod,valorprod-(valorprod*5/100)))
elif meio == 3:
    print('O valor do produto R${:.2f}, parcelado em 2X de R${:.2f}.'.format(valorprod,valorprod/2))
elif meio == 4:
    qparc = int(input('Quantas parcelas :'))
    prodcjuros = valorprod+(valorprod*20/100)
    valorparcela = prodcjuros / qparc
    print('O valor do produto R${:.2f}, Parcelado em {}x fica R${:.2f}\nValor das parcelas R${:.2f}'.format(valorprod,qparc,prodcjuros,valorparcela))
else:
    print('Codigo incorreto!!!')