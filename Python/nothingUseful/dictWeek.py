def getWeekDay(day):
    days = {
        1 : 'Domingo : Fim de semana',
        2 : 'Segunda : Dia de semana',
        3 : 'Terça : Dia de semana',
        4 : 'Quarta : Dia de semana',
        5 : 'Quinta : Dia de semana',
        6 : 'Sexta : Dia de semana',
        7 : 'Sábado : Fim de semana',
    }
    return days.get(day, 'Não é um dia da semana.')

if __name__ == '__main__':
    for day in range(7):
        print(f'{day+1} : {getWeekDay(day+1)}')