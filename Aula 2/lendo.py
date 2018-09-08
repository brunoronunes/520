#!/usr/bin/python3

# arquivo = open('nomes.txt', 'r')

# print(arquivo.read())

# arquivo.close()


nomes = ['yasmin','rafael','jessica']

# with open('nomes.txt', 'a') as arquivo:
#     arquivo.writelines([x+'\n' for x in nomes])

with open('nomes.txt', 'a') as arquivo:
    for nome in nomes:
        arquivo.writelines(nome +'\n')

