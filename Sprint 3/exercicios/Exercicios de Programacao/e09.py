primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for posicao, nomes in enumerate(primeirosNomes):
    print(f'{posicao} - {nomes} {sobreNomes[posicao]} está com {idades[posicao]} anos')
