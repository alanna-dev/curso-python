"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# digit_num = input('Digite um número: ')

# if digit_num.isdigit():
# 	digit_num_int = float(digit_num)
# 	if digit_num_int % 2 == 0:
# 		print(f'O número {digit_num} é par')
# 	else:
# 		print(f'O número {digit_num} é ímpar')
# else:
#     print('Você não digitou um número')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# hora = input('Digite a hora atual: ')

# try:
#     hora_int = int(hora)

#     if 0 <= hora_int <= 11:
#         print('Bom dia!')
#     elif 12 <= hora_int <= 17:
#         print('Boa tarde!')
#     elif 18 <= hora_int <= 23:
#         print('Boa noite!')
#     else:
#         print('Digite uma hora entre 0 e 23.')
    
# except:
#     print('Você não digitou um número inteiro')
    

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Digite seu primeiro nome: ')

tamanho_nome = len(nome)

if 1 <= tamanho_nome <= 4:
    print("Seu nome é curto")
elif 5 <= tamanho_nome <= 6:
    print("Seu nome é normal")
elif tamanho_nome > 6:
    print("Seu nome é muito grande")
else:
    print("Digite algo")
