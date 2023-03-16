"""
Argumentos nomeados e não nomeados em funções Python

Argumento nomeado tem nome com sinal de igual (por último)

Argumento não nomeado recebe apenas o argumento (valor)
Argumento posicional => depende da ordem (vem primeiro)
"""


# def soma(parâmetros):
#     print(x + y) manipular parâmetros
# 
# soma(argumentos para parâmetros)


def soma(x, y):
    print(x + y)
    
print(soma) # local da memória
soma(1, 2)
soma(y=1, x=2) # argumentos nomeados
