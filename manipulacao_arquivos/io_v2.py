#!python
arquivo = open('pessoas.csv')
for registro in arquivo:
    print('Nome:{} Idade:{}'.format(*registro.split(',')))

arquivo.close()
# print(*registro.split(','))
# print('Nome Do Curso:{}, Data conclusao:{}'.format(*registro.split(',')))
