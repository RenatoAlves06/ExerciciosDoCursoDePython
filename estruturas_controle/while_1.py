from random import randint

numero_informado = -1
numero_secreto = randint(0, 9)
total = 0


while numero_informado != numero_secreto:
    numero_informado = int(input('Digite um numero:  '))
    total += numero_informado
            


print('Numero secreto {} foi encontrado ! e soma de todos numeror é {}'.format(
    numero_secreto, total))
