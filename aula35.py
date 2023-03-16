nome = 'Alanna'
idade = 19
peso = 54.0
altura = 1.58
imc = peso / altura**2

print('{} tem {} de altura e pesa {}'.format(nome, altura, peso))
print('Imc: {:.2f}'.format(imc))

formato = '{n} tem {i} anos'
print(formato.format(n=nome, i=idade))