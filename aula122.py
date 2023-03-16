# copy - retorna uma cópia rasa (shallow copy)
# copia elementos imutáveis
# elementos mutáveis => cria cópia rasa

import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
d2 = d1.copy() #cópia rasa
d2 = copy.deepcopy(d1) #cópia profunda

d2['c1'] = 1000
d2['l1'][1] = 999999 # a lista também é alterada no copy 'd2'

print(d1)
print(d2)
