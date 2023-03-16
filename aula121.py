# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Alanna',
    'idade': 19,
    'endereços': [
        {'rua': 'a', 'numero': '111'},
        {'rua': 'b', 'numero': '222'},
    ],  
}

pessoa.setdefault('nome', 'NomeDefault')

print(pessoa['nome'])
print(len(pessoa))
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

