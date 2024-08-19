# %%

'''
Crie uma classe Calculo que contenha um método que
aceita dois parâmetros, X e Y, e retorne a soma dos dois. 
Nessa mesma classe, implemente um método de subtração, 
que aceita dois parâmetros, X e Y, e retorne a subtração
dos dois (resultados negativos são permitidos).
'''

class Calculo:
    def __init__(self, val):
        self.val = val
    
    def __add__(self, other):
        return self.val + other.val
    
    def __sub__(self, other):
        return self.val - other.val
    
x = Calculo(4) 
y = Calculo(5)

print(f'Somando: {x.val}+{y.val} = {x + y}')
print(f'Subtraindo: {x.val}-{y.val} = {x - y}')

# %%