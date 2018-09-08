#!/usr/bin/python3

with open('texto.txt', 'r') as arq:
    conteudo = arq.readlines()

aux = []

for x in conteudo:
    if x =='\n':
        continue
    aux.append(x)

with open('texto.txt', 'w') as arq:
    arq.writelines(aux)