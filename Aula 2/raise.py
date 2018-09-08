#!/usr/bin/python3

try:
    ling = input('Qual a melhor linguagem de programação? ')
    if ling.strip().lower() != 'python':
        raise ValueError('liaguagem errada')
    else:
        print('Muito bem')

except ValueError as e:
    print(e)

