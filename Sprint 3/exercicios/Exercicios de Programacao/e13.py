'''
Escreva um programa que lê o conteúdo do arquivo texto 
arquivo_texto.txt e imprime o seu conteúdo.
'''

with open('arquivo_texto.txt', 'rt') as arquivo:
    dados = arquivo.read()
    print(dados, end='')

'''
Obs: como não nos foi disponibilizado o download do arquivo arquivo_texto.txt,
esse código não funciona fora do ambiente do exércicio da Udemy.
'''