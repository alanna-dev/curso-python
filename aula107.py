"""
valores padrão para parâmetros
"""


def soma(x, y, z=None):
    if z is None:
        print(x + y)
    else:
        print(x + y + z)
        

soma(2, 1, 3)
