
arquivo = open('pessoas.csv')
dados = arquivo.read()
arquivo.close()
for registro in dados.splitlines():
    print('Nome:{},Idade:{}'.format(*registro.split(',')))

    # print(*registro.split(','))
    # print('Nome Do Curso:{}, Data conclusao:{}'.format(*registro.split(',')))
