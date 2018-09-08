#!/usr/bin/python3

qntd = int(input('Quantidade de notas: '))

soma = 0

for x in range(qntd):
    nota = int(input('Nota {}: '.format(x+1)))
    if nota > 10:
        print('Nota invalida!')
        qntd -= 1
        continue
    soma += nota

media = soma/qntd

if media >= 7:
    print('Media {}, aprovado'.format(media))
elif media >= 3:
    print('Media {}, recuperação'.format(media))
else:
    print ('Media {}, reprovado'.format(media))