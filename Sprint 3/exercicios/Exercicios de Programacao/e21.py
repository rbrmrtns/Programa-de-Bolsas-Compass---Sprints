# %%

'''
Implemente duas classes, Pato e Pardal, que herdam de
uma superclasse chamada Passaro as habilidades de voar
e emitir som.

Contudo, tanto Pato quanto Pardal devem emitir sons 
diferentes (de maneira escrita) no console, conforme o 
modelo a seguir.
'''

class Passaro:
    def __init__(self):
        pass
    
    def voar(self):
        print('Voando')
        
    def emitir_som(self):
        pass
    
class Pato(Passaro):
    def __init__(self):
        super().__init__()
        
    def emitir_som(self):
        print('Pato emitindo som...')
        print('Quack Quack')
        
class Pardal(Passaro):
    def __init__(self):
        super().__init__()
        
    def emitir_som(self):
        print('Pardal emitindo som...')
        print('Piu Piu')
        
pat1 = Pato()
par1 = Pardal()

print(pat1.__class__.__name__)
pat1.voar()
pat1.emitir_som()
print(par1.__class__.__name__)
par1.voar()
par1.emitir_som()

# %%