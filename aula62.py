contador = 0

while contador < 10:
    contador += 1
    
    if contador == 5:
        print('pulei o 5')
        continue #volta ao início do while
    
    print(contador)
    