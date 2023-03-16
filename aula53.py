"""
is / is not (tipo, valor, id)
"""

condicao = False
passou = None

if condicao:
    passou = True
    print('Faça algo')
else:
    print('Não faça algo')


if passou is None:
    print('Não passou no if')
else:
    print('Passou no if')
    
print(passou is None)
print(passou is not None)
