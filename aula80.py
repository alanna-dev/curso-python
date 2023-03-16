"""
listas
list => mutável
suporta vários valores de qualquer tipo
possui índice e fatiamento
métodos => append, insert, pop, del, clear, extend, +
"""

lista1 = list()

#         0       1       2    3    4
#        -5      -4      -3   -2   -1
lista2 = [1, 'Calannos', True, 4.0, []]

print(lista2[1], type(lista2[1]))

lista2[1] = 2
print(lista2[1], type(lista2[1]))
