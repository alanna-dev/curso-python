"""
formatação básica de strings
s - string
d - int
f - float
.<n de casas>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""

nome = 'Calannos'
print(f'{nome}.')
print(f'{nome:>5}.')
print(f'{nome:<5}.')
print(f'{nome:3^10}.')
print(f'{1001231.000236137123:0=+15,.2f}')
