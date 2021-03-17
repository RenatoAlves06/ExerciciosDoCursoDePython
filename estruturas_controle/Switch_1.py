

def get_dia_semana(dia):

    dias = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sabado',
    }
    return dias.get(dia, '** Dia invalido **')


if __name__ == '__main__':
    for dia in range(0, 9):
        if dia == 7 or dia == 1:
            print(dia, '* Fim De semana')
        elif dia < 1 or dia > 7:
            print(dia, 'x Dia invalido')
        else:
            print(f'{dia}*# Dia De Semana')
