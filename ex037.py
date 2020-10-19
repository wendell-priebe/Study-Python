# escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base de conversao: 1 para binario 2 para octal 3 para hexadecimal
print('\033[30m Conversor')
num = int(input('Digite um numero inteiro :'))
op = int(input( ' [1] Converter para binario\n [2] Converter para octal\n [3] Converter para hexadecimal\nOpçao [1], [2] ou [3] :\033[m'))
if op == 1:
    print(' O numero {} equivale a \033[4;33m{}\033[m em binario'.format(num,bin(num)[2:]))
elif op == 2:
    print(' O numero {} equivale a \033[4;33m{}\033[m em Octal'.format(num, oct(num)[2:]))
elif op == 3:
    print(' O numero {} equivale a \033[4;33m{}\033[m em Hexadecimal'.format(num, hex(num)[2:]))    #[2:] - começa a mostrar apartir da 3̣º casa
else:
    print('Opção invalida!')