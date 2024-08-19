# %%

'''
Verifique se cada uma das palavras da lista ['maça',
'arara', 'audio', 'radio', 'radar', 'moto'] é ou não
um palíndromo.
'''

palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for i in range(len(palavras)):
    
    comp = len(palavras[i]) // 2
    
    for j in range(comp):
        
        if palavras[i][j] != palavras[i][-(j + 1)]:
            
            print(f'A palavra: {palavras[i]} não é um palíndromo')
            break
            
    else:
        print(f'A palavra: {palavras[i]} é um palíndromo')

# %%