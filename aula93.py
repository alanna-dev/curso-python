# split - divide uma string
# join - une uma string
# strip, rstrip, lstrip - tira espaços

frase = '     olha só, que interessante    '
lista = frase.split(',')

lista_nova = []

for i, frase in enumerate(lista):
    lista_nova.append(lista[i].strip())
    
print(lista)
print(lista_nova)

frases_juntas = ', '.join(lista_nova) # join(iterável)
print(frases_juntas)
