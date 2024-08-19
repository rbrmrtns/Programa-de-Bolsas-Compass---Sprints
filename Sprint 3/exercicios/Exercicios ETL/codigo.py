# %%

# Função para divisão correta de colunas

def dividir_colunas(linha):
    colunas = []
    coluna_atual = []
    dentro_de_parenteses = False

    for char in linha:
        if char == '"':
            # Inverte o estado de dentro das aspas
            dentro_de_parenteses = not dentro_de_parenteses
        elif char == ',' and not dentro_de_parenteses:
            # Se uma vírgula fora das aspas for encontrada, finalize o campo atual
            colunas.append(''.join(coluna_atual).strip())
            coluna_atual = []
        else:
            # Adiciona o caractere ao campo atual
            coluna_atual.append(char)

    # Adiciona o último campo
    if coluna_atual:
        colunas.append(''.join(coluna_atual).strip())

    return colunas

# Etapa 1

nome = ''
qtde_filmes_max = 0

with open('actors.csv', 'r') as arquivo:
    for i, linha in enumerate(arquivo):
        if i > 0:    
            vals = dividir_colunas(linha)
            qtde_filmes_atual = int(vals[2])
            
            if qtde_filmes_atual > qtde_filmes_max:
                nome = vals[0]
                qtde_filmes_max = qtde_filmes_atual
            
with open('etapa-1.txt', 'w', encoding='utf-8') as resposta:
    resposta.write(f'O(a) ator/atriz com a maior quantidade de filmes é {nome}, \
sendo essa quantidade {qtde_filmes_max} filmes')


# Etapa 2

total_receita = 0.0
total_linhas = 0

with open('actors.csv', 'r') as arquivo:
    for i, linha in enumerate(arquivo):
        if i > 0:    
            vals = dividir_colunas(linha)
            receita = float(vals[5])
            
            total_receita += receita
            total_linhas += 1
            
with open('etapa-2.txt', 'w', encoding='utf-8') as resposta:
    resposta.write(f'A média da receita de bilheteria bruta dos principais filmes é de \
{(total_receita/total_linhas):.2f} milhões de dólares')
    
# Etapa 3

nome = ''
media_p_filme_max = 0.0

with open('actors.csv', 'r') as arquivo:
    for i, linha in enumerate(arquivo):
        if i > 0:    
            vals = dividir_colunas(linha)
            media_p_filme_atual = float(vals[3])
            
            if media_p_filme_atual > media_p_filme_max:
                nome = vals[0]
                media_p_filme_max = media_p_filme_atual
            
with open('etapa-3.txt', 'w', encoding='utf-8') as resposta:
    resposta.write(f'O(a) ator/atriz com a maior média de receita \
de bilheteria bruta por filme é {nome}, sendo essa média {media_p_filme_max} milhões de dólares')

# Etapa 4

filmes = set()

with open('actors.csv', 'r') as arquivo:
    for i, linha in enumerate(arquivo):
        if i > 0:    
            vals = dividir_colunas(linha)
            filme = vals[4]
            
            filmes.update({filme})
            
    filmes = list(filmes)
    filmes = {filmes[i]: 0 for i in range (len(filmes))}
    
with open('actors.csv', 'r') as arquivo:
    for i, linha in enumerate(arquivo):
        if i > 0:
            vals = dividir_colunas(linha)
            filme = vals[4]
            filmes[filme] = filmes.get(filme) + 1
    
    
    filmes = dict(sorted(filmes.items(), key=lambda item: (-item[1], item[0])))
            
with open('etapa-4.txt', 'w', encoding='utf-8') as resposta:
    for sequencia, (nome_filme, quantidade) in enumerate(filmes.items()):
        resposta.write(f'{sequencia} - O filme {nome_filme} aparece {quantidade} vez(es) no dataset\n')

# Etapa 5

atores = []
receitas_totais_brutas = []

with open('actors.csv', 'r') as arquivo:
    for i, linha in enumerate(arquivo):
        if i > 0:    
            vals = dividir_colunas(linha)
            atores.append(vals[0])
            receitas_totais_brutas.append(float(vals[1]))
            
    result = {atores[i]: receitas_totais_brutas[i] for i in range (len(atores))}
    result = dict(sorted(result.items(), key=lambda item: -item[1]))
    

with open('etapa-5.txt', 'w', encoding='utf-8') as resposta:
    for ator, receita in result.items():
            resposta.write(f'{ator} - {receita}\n')

# %%
