# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list

pessoa = {
    'nome': 'Alanna',
    'idade': 19,
    'endereços': [
        {'rua': 'a', 'numero': '111'},
        {'rua': 'b', 'numero': '222'},
    ],  
}

print(pessoa['endereços'])

for chave in pessoa:
    print(f'{chave}: {pessoa[chave]}')
