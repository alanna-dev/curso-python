# CRUD
# criar, ler, atualizar e apagar => lista [i]
# métodos => append, insert, pop, del, clear, extend, +

lista = [1, 2, 3]
print(lista)

lista.append(4)
print(lista)

del lista[2]
print(lista)

lista.insert(2, 8)
print(lista)

lista.pop(2)
print(lista)

lista_nova = [10, 12, 13]
lista.extend(lista_nova)
print(lista)

lista_mais = lista + lista_nova
print(lista_mais)

lista.clear()
print(lista)
