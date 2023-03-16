#iterar strings com while

nome = 'Alanna Farias'

tamanho = len(nome)
indice = 0
novo_nome = ''

while indice < tamanho:
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

print(novo_nome)
