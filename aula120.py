# manipulando chaves e valores em dicionários

pessoa = {}

chave = 'nome'
pessoa[chave] = 'Alanna'

print(pessoa[chave])

pessoa[chave] = 'Gil'

print(pessoa[chave])

del pessoa[chave]

print(pessoa.get('nome')) # None


