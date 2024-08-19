# %%

'''
Escreva uma função que recebe uma lista e retorna uma
nova lista sem elementos duplicados. Utilize a lista a seguir
para testar sua função.

['abc', 'abc', 'abc', '123', 'abc', '123', '123']
'''

def listaSemRepeticoes(lista):
    
    return list(set(lista))
    
print(listaSemRepeticoes(['abc', 'abc', 'abc', '123', 'abc', '123', '123']))

# %%