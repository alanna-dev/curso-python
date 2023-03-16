# Closure e funções que retornam outras funções
# Closure => Temos uma função definida dentro de outra função. \
# A função interna utiliza de parâmetros e variáveis da função externa


def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar


s1 = criar_saudacao('bom dia', 'alanna')

print(s1)
print(s1()) # closure
