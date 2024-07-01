#!/bin/bash

nmro_arquivo=1

touch relatorio_fina.txt
touch diretorios.txt

find . -name 'relatorio.txt' >> diretorios.txt

while IFS= read -r line
do
    echo "Relatorio ${nmro_arquivo}" >> relatorio_fina.txt
    cat $line >> relatorio_fina.txt
    echo "" >> relatorio_fina.txt
    nmro_arquivo=$((nmro_arquivo+1))
done < diretorios.txt

rm diretorios.txt