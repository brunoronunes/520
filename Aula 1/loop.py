#!/usr/bin/python3


lista = []
for x in range (97,123):
    lista.append(chr(x))

while lista:
    print(lista.pop(0))

print(lista)
