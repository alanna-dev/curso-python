# enumerate - enumera iteráveis (índices)

lista = ['a', 'b', 'c']

lista_enumerada = enumerate(lista)

for i in enumerate(lista, start=10):
    print(i)
    
for indice, letra in enumerate(lista):
    print(indice, letra)

# isso por baixo dos panos:
for tupla_enumerada in enumerate(lista):
    print('FOR da tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}')

# consome o iter:
for i in lista_enumerada:
    print(i)
