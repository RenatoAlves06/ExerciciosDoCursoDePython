# conceitos      notas
# A              De 10,0 á 9.1
# A-             De 9,0 á 8.1
# B              De 8,0 á 7.1
# B-             De 7,0 á 6.1
# C              De 6,0 á 5.1
# C-             De 5,0 á 4.1
# D              De 4,0 á 3.1
# D-             De 3,0 á 2.1
# E              De 2,0 á 1.1
# E-             De 1,0 á 0.0

# Para notas acima de 10 ser aconsiderado como invalidas

#! /usr/bin/python

def nota_conceito(valor):
    nota = float(valor)
    if nota > 10:
        return 'nota invalida'
    elif nota >= 9.1:
        return 'A'
    elif nota >= 8.1:
        return 'A-'
    elif nota >= 7.1:
        return 'B'
    elif nota >= 6.1:
        return 'B-'
    elif nota >= 5.1:
        return 'C'
    elif nota >= 4.1:
        return 'C-'
    elif nota >= 3.1:
        return 'D'
    elif nota >= 2.1:
        return 'D-'
    elif nota >= 1.1:
        return 'E'
    elif nota >= 0:
        return 'E-'
    else:
        return 'Nota invalida'


if __name__ == '__main__':
    valor_informado = input('NOTA ALUNO: ')
    conceito = nota_conceito(valor_informado)
    print(conceito)
