# Etapa 1 do Desafio: Remover as Linhas Duplicadas

1. Passo 1:

   Ler o arquivo CSV com o comando read_csv do Pandas

2. Passo 2:

   Usar o comando drop_duplicates para remover linhas duplicadas. O parâmetro "subset=None" serve para utilizar todas as colunas na comparação de diferença entre linhas e o "inplace=True" para efetivamente mudar o dataframe, portanto, eliminar as linhas duplicadas.

3. Passo 3:

   Sobreescrever o arquivo CSV com o dataframe atual. O parâmetro "index=False" serve para que o arquivo não contenha os indíces de cada linha.

# Etapa 2 do Desafio: Gráfico de Barras dos Top 5 Apps por Número de Instalações

## Código para Obter os Dados

1. Passo 1:

   Após ler o arquivo CSV com o comando read_csv do Pandas, percorrer o dataframe contendo os dados do arquivo e verificar se a string contendo a quantidade de instalações sem os caracteres especiais padrões ",", que dividem o número a cada 3 casas decimais, e "+", que indica que o número de instalações é superior ao que está registrado, é numérico, ou seja, é composta somente por caracteres númericos. Caso não seja, o id da linha que corresponde ao aplicativo é armanazenada na lista "apps_to_drop", que contém aplicativos a serem filtrados do resultado final. Caso seja, a string é transformada em int, para que a ordenação seja feita com valores numéricos, e não caracteres.

2. Passo 2:

   Retirar as linhas que correspondem aos aplicativos que não estão em um formato correto com o comando drop. Após isso, as linhas são ordenadas, primeiramente, pelos valores agora númericos da coluna "Installs" e depois pelos nomes dos aplicativos contidos na coluna "Apps". Finalmente, linhas com o mesmo valor na coluna "Apps", ou seja, linhas que correspondem a um mesmo aplicativo e diferem somente nos valores de quantidade de reviews, são removidas.

## Criação do Gráfico

1. Passo 1:

   Nomes dos aplicativos são armazenados na lista app_names e quantidades de instalações dos aplicativos são armazenados na lista app_installs para que sejam apresentados no gráfico. A posição vertical das barras é definida pelo comando arange do numpy, que gera uma lista de indíces igualmente distantes entre si a partir de um valor ou intervalo númerico, neste caso, o comprimento da lista app_nomes.

2. Passo 2:

   As barras do gráfico são definidas pelo comando barh, que tem como parâmetros a sua posição (posição no plano y), o seu comprimento (número de instalações) e alinhamento (centralizado). Os textos a esquerda das barras são definidos pelo comando set_yticks. O comando invert_yaxis é usado para colocar a barra de maior valor no topo do gráfico e a de menor valor na parte inferior. O texto do eixo x é definido com o comando set_xlabel e o título com o comando set_title.

3. Passo 3:

   As labels de cada barra são definidas com o comando bar_label, que tem como parâmetros o valor das barras que define o seu comprimento, isto é, seu valor númerico, e sua formatação. O limite do eixo x é definido pelo comando set_xlim, que recebe como valor máximo (right) a quantidade de instalações do aplicativo com mais instalações. Por fim, o gráfico é apresentado com o comando show do módulo matplotlib.pyplot.

# Etapa 3 do Desafio: Gráfico de Pizza das Categorias Existentes

## Código para Obter os Dados

1. Passo 1:

   Antes de mais nada, a função checarString é definida, a qual recebe como argumento uma string, percorre-a caractere por caractere e verifica se o caractere atual é um dígito númerico com o comando isdigit. Caso haja um único caractere numérico, ela retorna True, assim indicando que a string é inválida, já que, neste caso, os nomes das categorias só podem ser compostas por letras e caracteres especiais.

2. Passo 2:

   Após ler o arquivo CSV com o comando read_csv do Pandas, percorrer o dataframe contendo os dados do arquivo e verificar se a string contendo a categoria possui algum caractere numérico. Caso possua, o id da linha que corresponde ao aplicativo é armanazenada na lista "apps_to_drop", que contém aplicativos a serem filtrados do resultado final.

3. Passo 3:

   Retirar as linhas que correspondem aos aplicativos que não estão em um formato correto com o comando drop. Após isso, usa-se o comando groupby do Pandas para agrupar as linhas por categoria e depois contar as ocorrências das outras colunas que compartilham o mesmo valor na coluna categoria (Category no arquivo CSV e, consequentemente, no dataframe) com o comando count.

## Criação do Gráfico

1. Passo 1:

   As categorias são armazenados na lista app_category, quantidades de aplicativos por categoria são armazenados na lista app_category_count e somadas a variável app_category_total_count, que armazena o total de aplicativos com a coluna categoria não-nula. A porcentagem da quantidade de aplicativos de uma categoria em relação ao total de aplicativos com categoria é calculada para cada categoria e armazenada na lista app_category_percentage.

2. Passo 2:

   As labels, que são uma string composta pelo nome da categoria e sua porcentagem, são geradas com list comprehension.

3. Passo 3:

   O texto do título é definido com o comando set_title. O gráfico de pizza é criado com o comando pie, o qual recebe os argumentos app_category_percentage (lista das porcentagens de cada aplicativo) e radius (raio do círculo em centímetros). A legenda é criado pelo comando legend, que recebe as labels criadas anteriormente, tem a localização definida para o centro esquerdo pelo parâmetro "loc='center left'" e é contida por uma caixa, o que definido pelo parâmetro bbox_to_anchor. Por fim, o gráfico é apresentado com o comando show da biblioteca matplotlib.pyplot.

# Etapa 4 do Desafio: Mostrar App mais Caro Existente

1. Passo 1:

   Após ler o arquivo CSV com o comando read_csv do Pandas, percorrer o dataframe contendo os dados do arquivo e passá-los pelas estruturas de controle IF ELSE a seguir:

   - Verificar se a valor da coluna preço (Price no dataframe) é uma string.
     - Caso seja, verificar se a string começa com $ ou, caso 1 ponto final seja retirado da string, ela só contenha valores númericos (isdigit).
       - Caso essa condição seja verdadeira, verificar se o valor da string convertida para float é maior que o valor localmente armazenado de maior preço de aplicativo.
         - Caso essa condição seja verdadeira, a lista contendo os ids dos aplicativos de maior preço, denominada most_expensive, é limpa, o id do aplicativo atual é adicionada à lista e o valor da variável que armazena o maior preço, most_expensive_price, é atualizado.
         - Caso o seu valor convertido para float seja igual àquele armazenado na variável de maior preço, o id do aplicativo atual é adicionado à lista de aplicativos de maior preço.
   - Caso o valor da coluna preço não seja uma string, verificar se ele é int ou float.
     - Caso qualquer uma das alternativas seja verdadeira, verificar se o valor númerico convertido para float é maior que o valor localmente armazenado de maior preço de aplicativo.
       - Caso essa condição seja verdadeira, a lista contendo os ids dos aplicativos de maior preço, denominada most_expensive, é limpa, o id do aplicativo atual é adicionada à lista e o valor da variável que armazena o maior preço, most_expensive_price, é atualizado.
       - Caso o seu valor convertido para float seja igual àquele armazenado na variável de maior preço, o id do aplicativo atual é adicionado à lista de aplicativos de maior preço.

2. Passo 2:

   Uma vez que os id(s) do(s) aplicativo(s) mais caro(s) esteja(m) armazenado(s) na lista most_expensive, fazer um for de comprimento da lista most_expensive e mostrar o nome e preço da linha de id correspondente ao(s) id(s) armazenado(s) na lista de aplicativos de maior preço.

# Etapa 5 do Desafio: Mostrar Quantos Apps têm Classificação 'Mature 17+'

1. Passo 1:

   Após ler o arquivo CSV com o comando read_csv do Pandas, usar o comando groupby do Pandas para agrupar as linhas por classificação indicativa e depois contar as ocorrências das outras colunas que compartilham o mesmo valor na coluna classificação indicativa (Content Rating no arquivo CSV e, consequentemente, no dataframe) com o comando count.

2. Passo 2:

   Converter o valor da coluna App, que agora contém a quantidade de nome de apps de linhas que possuem como valor da coluna classificação indicativa "Mature 17+", para string, assim podendo ser concatenada, ao texto final e apresentá-lo.

# Etapa 6 do Desafio: Mostrar Top 10 Apps por Número de Reviews

1. Passo 1:

   Após ler o arquivo CSV com o comando read_csv do Pandas, percorrer o dataframe contendo os dados do arquivo e verificar se a string contendo o número de reviews é composta somente por valores númericos com o comando isdigit. Caso essa condição seja falsa, o id da linha que corresponde ao aplicativo é armanazenada na lista "apps_to_drop", que contém aplicativos a serem filtrados do resultado final, já caso a condição seja verdadeira, esse valor string é convertido para int, assim permitindo, posteriormente, uma ordenação por valores númericos, e não baseados na tabela ASCII.

2. Passo 2:

   Retirar as linhas que correspondem aos aplicativos que não estão em um formato correto com o comando drop. Após isso, usa-se o comando sort_values do Pandas para ordenar as linhas que correspondem a cada aplicativo primeiro pelo valor da coluna "Reviews" e, depois, pelo valor da coluna "App". Esse comando também recebe os parâmetros "ascending=False", assim fazendo a ordenação decrescente, e "na_position='last'", para que as linhas com NaN na(s) determinada(s) coluna(s) fiquem abaixo das outras. Linhas com o mesmo valor para a coluna "App" são eliminadas com o comando drop_duplicates(subset=['App']) e o comando head(10) é usado para atribuir ao dataframe somente as suas 10 primeiras linhas.

3. Passo 3:

   Com o comando iterrows, são obtidos os valores de índice e das colunas de cada linha do dataframe, podendo ser apresentados com o comando print.

# Etapa 7 do Desafio: Criar Mais 2 Cálculos Sobre o Dataset

## Lista gerada: Top 10 Gêneros Mais Frequentes

1. Passo 1:

   Antes de mais nada, a função checarString é definida, a qual recebe como argumento uma string, percorre-a caractere por caractere e verifica se o caractere atual é um dígito númerico com o comando isdigit. Caso haja um único caractere numérico, ela retorna True, assim indicando que a string é inválida, já que, neste caso, os nomes dos gêneros só podem ser compostas por letras e caracteres especiais.

2. Passo 2:

   Após ler o arquivo CSV com o comando read_csv do Pandas, percorrer o dataframe contendo os dados do arquivo e verificar se a string contendo a gênero possui algum caractere numérico. Caso possua, o id da linha que corresponde ao aplicativo é armanazenada na lista "apps_to_drop", que contém aplicativos a serem filtrados do resultado final. Em sequência, retirar as linhas que correspondem aos aplicativos que não estão em um formato correto com o comando drop.

3. Passo 3:

   Usar o comando unique para capturar somente valores únicos da coluna "Genres" e armazená-los na lista genres. O conjunto unique_genres é criado, o qual é atualizado com os valores da lista genres divididos pelo caractere ";", assim eliminando valores repetidos de entrarem no conjunto final, já que os valores do coluna gêneros, muitas vezes, eram compostos por mais de um gênero de uma única vez. O conjunto unique_genres resultante é transformado em lista e ordenado por ordem alfábetica pelo comando sort. Por fim, unique_genres é transformado em um dicionário, que tem como índice o nome dos gêneros e valor a contagem de ocorrências dos gêneros, as quais, no momento de sua criação, estão todas zeradas.

4. Passo 4:

   Percorre-se o dataframe e é verificado se a string da coluna gêneros da linha de id i possui um ";" ou não. Caso ela possua, a lista genres recebe a sua divisão por ";" e é verificado se o valor da lista na determinado posição é ou não um índice presente no dicionário unique_genres. Caso seja, o item de índice igual àquela string da lista tem o seu valor acrescido de 1. Agora, caso não se encontre um ";", é feito praticamente o mesmo processo, mas sem a divisão por ";" e compara-se somente com um valor de gênero.

5. Passo 5:

   unique_genres recebe um novo dicionário com o comando dict, o qual recebe um dicionário ordenado pelo comando sorted, que recebe os argumentos os itens de unique_genres, a chave uma função lambda "item: item[1]", logo fazendo com a ordenação seja pelo item na posição 1, ou seja, o valor e não o índice, e "reverse=True", para que a ordenação seja decrescente. Depois disso, é feita uma lista de unique_genres, lista essa que é composta pelos itens de unique_genres de posição 0 a 9, e tal lista é convertida para um dicionário e atribuída para unique_genres.

6. Passo 6:

   Com o comando items, são obtidos os valores de índice e de valor de cada dupla de unique_genres, podendo ser apresentadas com o comando print.

## Valor calculado: Quantidade de Aplicativos Gratuitos

1. Passo 1:

   Após ler o arquivo CSV com o comando read_csv do Pandas, usar o comando groupby do Pandas para agrupar as linhas por tipo e depois contar as ocorrências das outras colunas que compartilham o mesmo valor na coluna tipo (Type no arquivo CSV e, consequentemente, no dataframe) com o comando count.

2. Passo 2:

   Converter o valor da coluna App, que agora contém a quantidade de nome de apps de linhas que possuem como valor da coluna tipo "Free", para string, assim podendo ser concatenada, ao texto final e apresentá-lo.

# Etapa 8 do Desafio: Criar Outras 2 Formas Gráficas

## 1º Gráfico Escolhido: Gráfico de Dispersão Baseado no Top 10 Apps por Número de Reviews

1. Passo 1:

   As posições dos pontos no eixo x do gráfico são definidas pelo comando arange do numpy, que gera uma lista de indíces igualmente distantes entre si a partir de um valor ou intervalo númerico, neste caso, um intervalo de 1 ao comprimento do dataframe + 1. Já as posições no eixo y são definidas pelo número de reviews de cada linha de id i, encontradas nos valores de x - 1. Por fim, as cores são definidas de forma aleátorio pelo comando rand do módulo random do Numpy. A média simples de instalações por aplicativo é calculada usando o comando mean do Numpy nos valores de y e multiplicada pelo comprimento de x.

2. Passo 2:

   O gráfico de dispersão é gerado com o comando scatter do matplotlib.pyplot, recebendo como argumentos as listas x, y e colors, e a linha que representa a média de instalações por aplicativo é criada com o comando plot, o qual recebe os argumentos a lista x, o valor y e a label "Média de Reviews".

3. Passo 3:

   Partindo para os textos do gráfico, a lista apps_names é gerada com list comprehension, seguindo a condição de que caso o nome de um aplicativo ultrapasse 10 caracteres, a string deve ser cortado após o décimo caractere e concatenada à string "..." e, caso essa condição seja falsa, o nome segue inalterado. O título do gráfico é definido com o comando set_title, o texto do eixo x com o comando xlabel e o do eixo y com o comando ylabel. Para cada ponto, é usado o comando annotate para colocar o nome de seu respectivo aplicativo ao seu lado, comando esse que recebe como argumentos o nome do aplicativo, presente na lista apps_names, e as coordenadas do ponto nos eixo x e y. A legenda da linha da média é criada com o comando legend, que tem como parâmetro "loc='upper right'", para que fique no canto superior direito do gráfico. Por fim, o gráfico é apresentado com o comando show do módulo matplotlib.pyplot.

## 2º Gráfico Escolhido: Gráfico de Linhas Baseado no Top 10 Gêneros Mais Frequentes

1. Passo 1:

   As posições dos pontos da linha no eixo x do gráfico são definidas pelo comando arange do numpy, que gera uma lista de indíces igualmente distantes entre si a partir de um valor ou intervalo númerico, neste caso, um intervalo de 1 ao comprimento do dataframe + 1. Já as posições no eixo y são definidas pelo quantidade de aplicativos daquele gênero, encontradas ao se converter os valores de unique_genres para uma lista.

2. Passo 2:

   A linha é criada com o comando plot, o qual recebe os argumentos a lista x, o valor y e a marcador "o", o qual representa um círculo.

3. Passo 3:

   Partindo para os textos do gráfico, a lista categories_names é gerada com list comprehension, a qual recebe os nomes dos gêneros, encontrados ao se converter os índices de unique_genres para uma lista. O título do gráfico é definido com o comando set_title, o texto do eixo x com o comando xlabel e o do eixo y com o comando ylabel. Para cada ponto da linha, é usado o comando annotate para colocar o nome de seu respectivo gênero ao seu lado, comando esse que recebe como argumentos o nome do gênero, presente na lista categories_names, e as coordenadas do ponto nos eixo x e y. Por fim, o gráfico é apresentado com o comando show do módulo matplotlib.pyplot.
