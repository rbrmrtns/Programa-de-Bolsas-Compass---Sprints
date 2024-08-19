# Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.

import json

with open('person.json', 'r') as person:
    person_data = json.load(person)
    print(person_data)

'''
Obs: como não nos foi disponibilizado o download do arquivo person.json,
esse código não funciona fora do ambiente do exércicio da Udemy.
'''