# Explicação do Desafio 6

## Código Python

- Após os imports, são definadas as funções criar_bucket, que recebe o nome do bucket, tenta criá-lo no S3 e retorna um erro caso ocorra; e carregar_arquivo, que recebe os dados de um objeto, neste caso os dados do arquivo que será lido, o nome do bucket em que ele será carregado e a "key do arquivo", que é composta dos diretórios e do nome e tipo do arquivo, tenta carregar o arquivo e retorna um erro caso ocorra.
- O nome do bucket é inserido na variável bucket e o horário do processamento é armazenado na variável timestampProcessamento. A partir daí, as variáveis anoProcessamento, mesProcessamento e diaProcessamento recebem os valores de ano, mês e dia contidas na variável timestampProcessamento, respectivamente.
- A key, ou seja, nome, tipo e diretórios em que o arquivo está contido, de ambos arquivos é definida, seguindo o padrão informado no desafio.
- O bucket é criado, os arquivos CSVs são abertos com o encoding UTF-8, o qual aceita caracteres especiais, lidos e inseridos no bucket criado anteriormente.

## Configurações de acesso AWS

Para que o boto3 funcione, é preciso definir os credenciais e configurações de acesso e inseri-los em arquivos numa pasta .aws. Como uso o Windows, os arquivos foram colocados no seguinte diretório: C:\Users\User\\.aws.

Conteúdo do arquivo de credenciais (credentials), censurado para a não-exposição de dados sensíveis. É importante frisar que a aws_secret_acess_key é atualizada periodicamente e deve ser alterado no arquivo para que o código possa ser executado:
![Arquivo Credentials](/Sprint%206/evidencias/credentials.png)

Conteúdo do arquivo de configurações (config):\
![Arquivo Config](/Sprint%206/evidencias/config.png)

## Docker

A imagem desafio6 é criada a partir da imagem do Python 3, a qual primeiramente atualiza as bibliotecas default do Python 3, define a pasta /app como a pasta de trabalho, copia os arquivos Dockerfile, script.py e os CSVs movies.csv e series.csv para o contêiner, instala a biblioteca boto3 e executa o código presente no arquivo script.py.

O seguinte comando foi utilizado para criar a imagem desafio6:
![Criação Imagem](/Sprint%206/evidencias/comando-criacao-imagem.png)

Já este comando foi utilizado para criar e executar o contêiner desafio6-container, baseado na imagem desafio6. "-v C:/Users/User/.aws:/root/.aws" foi adicionado ao comando para copiar as chaves de acesso ao contêiner, para que ele possa manipular o S3, e "-v csvs_volume:/app/csvs" para que os arquivos CSVs sejam armazenados no volume csvs_volume:
![Execução Contêiner](/Sprint%206/evidencias/comando-execucao-container.png)

## Resultado

Como se pode ver abaixo, os arquivos movies.csv e series.csv foram armazenados no bucket S3, dentro do padrão de diretórios presente no material do desafio:

![movies.csv](/Sprint%206/evidencias/carregamento-movies-csv.png)

![series.csv](/Sprint%206/evidencias/carregamento-series-csv.png)
