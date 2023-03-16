"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""

#codigo procedural

import re
import sys

cpf = '746.824.890-70' \
    .replace('.', '') \
    .replace('-', '')
    
# cpf = re.sub(
#     r'[^0-9]',
#     '',
#     '746.824.890-70'
# )

# cpf2 = cpf.split('.')
# cpf3 = cpf2[2].split('-')
# del cpf2[2]
# cpf_final = cpf2 + cpf3

entrada_sequencia = cpf == cpf[0] * len(cpf)

if entrada_sequencia:
    print('você digitou dados sequenciais.')
    sys.exit() #sai do python

nove = cpf[:9]
multiplicador = 10
soma_final = 0

for digito1 in nove:
    digito1 = int(digito1) * multiplicador
    multiplicador -= 1
    soma_final = soma_final + digito1

digito1 = (soma_final * 10) % 11

if digito1 <= 9:
    digito1 = digito1
else:
    digito1 = 0


dez = cpf[:10]
multiplicador2 = 11
soma_final2 = 0

for digito2 in dez:
    digito2 = int(digito2) * multiplicador2
    multiplicador2 -= 1
    soma_final2 = soma_final2 + digito2

digito2 = (soma_final2 * 10) % 11

if digito2 <= 9:
    digito2 = digito2
else:
    digito2 = 0
    
cpf_calculo = f'{nove}{digito1}{digito2}'

if cpf == cpf_calculo:
    print('valido')
else:
    print('invalido')
