# operação ternária (condicional de uma linha)
# <valor> if <condição> else <outro valor>

print('a' if True else 'b')

digito = 9  # > 9 = 0
novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)
