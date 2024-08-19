# %%

'''
Escreva uma função que recebe como parâmetro uma lista e
retorna 3 listas: a lista recebida dividida em 3 partes iguais.
'''

def divisor_lista(lista):
    compasso = len(lista) // 3
    val_ini = 0
    val_fin = compasso
    
    listas = [[], [], []]
    
    for i in range(3):
        listas[i] = lista[val_ini:val_fin]
        
        val_ini += compasso
        val_fin += val_fin
        
    return listas[0], listas[1], listas[2]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

lista1, lista2, lista3 = divisor_lista(lista)

print (lista1, lista2, lista3)

# %%