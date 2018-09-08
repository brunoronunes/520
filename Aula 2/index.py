#!/usr/bin/python3

convidados = ['daniel','maria','joao']

try:
    num = int(input('Digite posição do convidado: '))
    print(convidados[num -1])
except IndexError:
    print('Só existem {} convidados na sua lista!'.format(len(convidados)))
except ValueError:
    print('Digite apenas números')
except Exception as e:
    print('Erro: {}'.format(e))

