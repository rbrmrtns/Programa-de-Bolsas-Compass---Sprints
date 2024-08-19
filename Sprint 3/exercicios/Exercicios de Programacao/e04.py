# %%

'''
Escreva um código Python para imprimir todos os números
primos entre 1 até 100. Lembre-se que você deverá
desenvolver o cálculo que identifica se um número é primo
ou não.
'''

for i in range(1, 101):
    
    if i > 1:
        
        for j in range (2, (i // 2) + 1):
            
            if (i % j == 0):
                break
        
        else:
            print(i)

# %%