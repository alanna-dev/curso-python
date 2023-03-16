"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os

palavra_secreta = 'amor'
palavra_descoberta = ''
tentativas = 0

while palavra_descoberta != palavra_secreta:
    adivinhar = input('digite uma letra: ')
    tentativas += 1
    
    if len(adivinhar) > 1:
        print('digite somente uma letra.')
    
    if adivinhar in palavra_secreta:
        palavra_descoberta += adivinhar
    
    palavra_final = ''
    for adivinhar in palavra_secreta:
        if adivinhar in palavra_descoberta:
            palavra_final += adivinhar
        else:
            palavra_final += '*'
    print(palavra_final)
    
    if palavra_descoberta == palavra_secreta:
        os.system('cls')
        print(f'Você acertou, a palavra secreta era "{palavra_final}"!')
        print(f'Número de tentativas: {tentativas}')
    
