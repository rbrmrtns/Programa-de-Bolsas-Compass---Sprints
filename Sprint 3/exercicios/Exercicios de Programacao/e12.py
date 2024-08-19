# %%

'''
Implemente a função my_map(list, f) que recebe uma
lista como primeiro argumento e uma função como segundo
argumento. Esta função aplica a função recebida para cada
elemento da lista recebida e retorna o resultado em uma
nova lista.
'''

def my_map(list, f):
    for i in range(len(list)):
        list[i] = f(list[i])
        
    return list
    
def ao_quadrado(num):
    
    return num ** 2
    
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(my_map(lista, ao_quadrado))
