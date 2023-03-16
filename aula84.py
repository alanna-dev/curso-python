"""
copiado o valor (imutáveis)
aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Alanna', 'Carlos']
lista_b = lista_a

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)

lista_a = ['Alanna', 'Carlos']
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
