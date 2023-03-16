"""
try / except
try - tentar executar
except - ocorreu algum erro ao tentar executar
"""

num = input('digite um número: ')

try:
    num_int = int(num) #fail fast
    print(num_int)
    print(f'o dobro de {num} é {num_int * 2:.2f}')
except:
    print('ísso não é um número') 
