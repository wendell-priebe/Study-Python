# faça um algoritimo que leia o preço da um produto e mostre seu novo preço com 5% de desconto
print('\033[31mCompras acima de R$700.00 com desconto de 15%!!!\ncampras abaixo de R$700.00 considerar 5% de desconto '
      '\033[m')
prod1 = float(input('Valor do produto: R$'))
um = int(input('Informe 1 para continuar comprando ou 0 para finalizar compra:'))
if um == 1:
    prod2 = float(input('Valor do produto: R$'))
    dois = int(input('Informe 1 para continuar comprando ou 0 para finalizar compra:'))
    if dois == 1:
        prod3 = float(input('Valor do produto: R$'))
        total = prod1 + prod2 + prod3
        if total >= 700:
            desconto1 = total - (total * 15 / 100)
            print('Valor total de produtos R${:.2f}\n com desconto de 15% você pagara R${:.2f}'.format(total,desconto1))
        else:
            desconto2 = total - (total * 5 / 100)
            print('Valor total de produtos R${:.2f}\n com desconto de 5% você pagara R${:.2f}'.format(total, desconto2))

