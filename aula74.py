"""
iterável => str, range, etc (__iter__)
iterador => quem sabe entregar um valor por vez
next => me entregue o próximo valor
iter => me entregue seu iterador
"""

texto = iter('Calannos') #.__iter__()
print(texto) #iterador

print(texto.__next__())
print(next(texto))

# for letra in texto:
    # chama o iter() do texto
    # chama o next()
    # break quando levantar a exception StopIteration
 
# como for trabalha em código:
texto = 'Luiz'

iteratador = iter(texto)

# isto
while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break

# é isso:
for letra in texto:
    print(letra)
