"""
repetições:
while => enquanto a condição for verdadeira
      => utilizar quando não souber precisamente/
         quantas repetições terá
"""

condicao = True
while condicao:
    nome = input('digite seu nome: ')
    print(nome)
    
    if nome == 'sair':
    	break
