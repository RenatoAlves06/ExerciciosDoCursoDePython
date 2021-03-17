#!python
try:
    arquivo = open('pessoas.csv')

    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
except IndexError:  # ignorar erro
    pass  # bloco vazio

finally:
    arquivo.close()

if arquivo.closed:
    print('Arquivo foi fechado')

# print(*registro.split(','))
# print('Nome Do Curso:{}, Data conclusao:{}'.format(*registro.split    (',')))
