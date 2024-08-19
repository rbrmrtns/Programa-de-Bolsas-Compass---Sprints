# %%

'''
Desenvolva um código em Python que crie variáveis para
armazenar o nome e a idade de uma pessoa, juntamente
com seus valores correspondentes. Como saída, imprima o
ano em que a pessoa completará 100 anos de idade.
'''

from datetime import datetime

nome = 'Maria'
idade = 10

ano = datetime.now().year

print(int(ano) + (100 - idade))

# %%