# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Alanna',
    'idade': 19,
}

print(pessoa.get('nome'))

# nome = pessoa.pop('nome')
# print(nome)
# print(pessoa)

ult_chave = pessoa.popitem()
print(ult_chave)
print(pessoa)

# pessoa.update({
#     'nome': 'novo nome'
# })

# tupla_atualizacao = ('nome', 'novo nome'), ('idade', 20)

pessoa.update(nome='novo nome', idade=20)

print(pessoa)
