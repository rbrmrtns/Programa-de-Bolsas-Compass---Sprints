# %%

'''
Calcule o valor mínimo, valor máximo, valor médio e a
mediana da lista gerada na célula abaixo:

Obs.: Lembrem-se, para calcular a mediana a lista deve
estar ordenada!
'''

import random

random_list = random.sample(range(500), 50)

mediana = 0
media = 0
valor_minimo = 0
valor_maximo = 0

random_list.sort()

if len(random_list) % 2 != 0:
    mediana = random_list[len(random_list) // 2]
    
else:
    mediana = (random_list[len(random_list) // 2 - 1] + random_list[len(random_list) // 2]) / 2
    
media = sum(random_list) / len(random_list)

valor_minimo = min(random_list)

valor_maximo = max(random_list)

print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')

# %%