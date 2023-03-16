""" 
laço de repetição => for
for quer um iterável => vai acessar cada elemento /
do que você pediu por vez
"""

texto = 'Python'
palavra_nova = ''

for letra in texto:   #para cada letra em um iterável (texto)
    palavra_nova += f'*{letra}'    #faça isso

print(palavra_nova)
