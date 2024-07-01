#!/bin/bash

arquivo_valor="/tmp/valor.dat"

# se nao tiver um arquivo, comecar do zero
if [ ! -f "$arquivo_valor" ]; then
    valor=0

# caso contrario, ler o valor do arquivo
else
    valor=$(cat "$arquivo_valor")
fi

valor=$((valor + 1))

data_execucao=$(date +"%Y%m%d") 
timestamp_execucao=$(date +"%Y/%m/%d %H:%M")

mkdir vendas${valor}
cp dados_de_vendas.csv ./vendas${valor}/
cd ./vendas${valor}/
mkdir backup
cp dados_de_vendas.csv ./backup/dados-${data_execucao}.csv
cd ./backup/
mv dados-${data_execucao}.csv backup-dados-${data_execucao}.csv
touch relatorio.txt
echo "Data do sistema operacional: ${timestamp_execucao}" >> relatorio.txt
awk -F ',' 'NR==2{print "Data do primeiro registro de venda: "$5}' backup-dados-${data_execucao}.csv >> relatorio.txt
awk -F ',' 'END{print "Data do ultimo registro de venda: "$5}' backup-dados-${data_execucao}.csv >> relatorio.txt
echo "Quantidade de itens diferentes vendidos: $(tail -n+2 backup-dados-${data_execucao}.csv | wc -l)" >> relatorio.txt
head -n10 backup-dados-${data_execucao}.csv
head -n10 backup-dados-${data_execucao}.csv >> relatorio.txt
tar -czvf backup-dados-${data_execucao}.tar.gz backup-dados-${data_execucao}.csv
rm backup-dados-${data_execucao}.csv
cd ..
rm dados_de_vendas.csv

echo "${valor}" > "$arquivo_valor"