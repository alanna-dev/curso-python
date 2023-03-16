import sys

cpf = input('digite um cpf: ') \
    .replace('.', '') \
    .replace('-', '')

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
