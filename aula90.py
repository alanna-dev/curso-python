lista = []

while True:
    escolher = input('[i]inserir [a]apagar [l]listar [s]sair: ')
    if escolher == 'i':
        inserir = input('digite o que deseja inserir: ')
        lista.append(inserir)
    elif escolher == 'a':
        apagar = input('digite o indice do que deseja apagar: ')
        
        try:
            indice = int(apagar)
            del lista[indice]
        except ValueError:
            print('digite um número')
        except IndexError:
            print('esse índice não existe')
        
    elif escolher == 'l':
        if len(lista) > 0:
            
            for i, produto in enumerate(lista):
                print(i,produto)
        else:
            print('não há nada na lista')
            
    elif escolher == 's':
        print('Você saiu.')
        break
        
    else:
        print('escolha uma das opções')
        continue
