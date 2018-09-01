#!/usr/bin/python3
nota1 = int(input('Nota 1: '))
nota2 = int(input('Nota 2: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print('Media {}, aprovado'.format(media))
elif media >= 3:
    print('Media {}, recuperação'.format(media))
else:
    print ('Media {}, reprovado'.format(media))