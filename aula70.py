frase = 'o Python é uma linguagem de programação é multiparadigma.' \
    'Python foi criado por Guido van Rossum'.lower()

i = 0
quant_letra = 0
letra_final = ''
while i < len(frase):
    letra = frase[i]
    
    if letra == ' ':
        i += 1
        continue
    
    quant = frase.count(letra)
    
    if quant_letra < quant:
        quant_letra = quant
        letra_final = letra
    
    i += 1

print(f'a letra "{letra_final}" apareceu {quant_letra} vezes')
