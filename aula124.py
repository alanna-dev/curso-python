# sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

# for indice in perguntas:
#     for chave in indice:
#         print(indice.get(chave))

for pergunta in perguntas:
    print(pergunta['Pergunta'])
    for indice, opcoes in enumerate(pergunta['Opções']):
        print(f'[{indice}]{opcoes}')

    escolha = input('Digite a opção certa: ')
    escolha_int = int(escolha)

    if escolha_int == pergunta['Resposta']:
        print('Resposta correta')
    else:
        print('Resposta errada')
