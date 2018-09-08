#!/usr/bin/python3

try:
    qntd = int(input('Quantidade de notas: '))
except Exception as e:
    print (e)
    print("Digite somente números")
    exit(0)

soma = 0

for x in range(qntd):
    try:
        nota = int(input('Nota {}: '.format(x+1)))
    except Exception:
        print('Digite somente números!')
        exit()
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