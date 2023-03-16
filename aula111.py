# *args => argumentos não nomeados
#       => empacotamento e desempacotamento

# args empacota o que mandar para a função dentro de uma tupla
# 
# desempacota uma tupla para enviar como parâmetros para uma função
# 	numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
# 	(*numeros)

# x, y, *resto = 1, 2, 3, 4, 5, 6
# print(x, y, resto)


# def soma(x, y):
#     print(x, y)
    
    
def soma(*args):
    print(args, type(args))


soma(1, 2, 3, 4, 5, 6)

print(sum((1, 2, 3, 4, 5, 6)))

numeros = 1, 2, 3, 4, 5, 6
print(*numeros)
