# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.


def multiplicador(multiplicador):
    def multiplica(numero):
        return f'{multiplicador} x {numero} = {multiplicador * numero}'
    return multiplica


r1 = multiplicador(5)

print(r1(4))
