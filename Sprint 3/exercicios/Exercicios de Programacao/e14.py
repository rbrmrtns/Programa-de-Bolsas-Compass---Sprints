# %%

'''
Escreva uma função que recebe um número variável de
parâmetros não nomeados e um número variado de
parâmetros nomeados e imprime o valor de cada parâmetro
recebido.
'''

def vals_params(*args, **kwargs):
    
    for v in args:
        print(v)
    
    for k, v in kwargs.items():
        print(v)
    
vals_params(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

# %%