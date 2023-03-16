# calculadora com while

while True:
    numero1 = input('digite um número: ')
    numero2 = input('digite outro número: ')
    operador = input('digite o operador (+ - * ou /): ')
    
    entrada_valida = None
    operadores_validos = '+-*/'
    numero1_float = 0
    numero2_float = 0
    
    try:
        numero1_float = float(numero1)
        numero2_float = float(numero2)
        entrada_valida = True
    except:
        entrada_valida = None
        
    if entrada_valida is None:
        print('você digitou algum número ou operador inválido.') 
        continue
    elif len(operador) > 1:
        print('digite apenas um operador.')
        continue
    elif operador not in operadores_validos:
        print('operador inválido.')
        continue
    
    
    if operador == '+':
        print(f'{numero1} + {numero2} = {numero1_float + numero2_float:.2f}')
    elif operador == '-':
        print(f'{numero1} - {numero2} = {numero1_float - numero2_float:.2f}')
    elif operador == '*':
        print(f'{numero1} * {numero2} = {numero1_float * numero2_float:.2f}')
    elif operador == '/':
        print(f'{numero1} / {numero2} = {numero1_float / numero2_float:.2f}')
    
    
    sair = input('Deseja sair? [s]sim: ').lower().startswith('s')
    
    if sair is True:
        break
