#!python

with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome:{}, Idade:{}'.format(*pessoa), file=saida)

if saida.closed:
    print('Saida OK')

if arquivo.closed:
    print('saida ok')
