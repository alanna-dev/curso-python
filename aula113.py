# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


def multiplicacao(*args):
    resultado = 1        # se total=0 => zera o cálculo
    for numero in args:
        resultado *= numero
    return resultado


m1 = multiplicacao(1, 2, 3)
print(m1)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.


def impar_par(numero):
    if numero % 2 == 0:
        return 'par'
    return 'impar'
    

m2 = impar_par(5)
print(m2)
