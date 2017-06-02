def find_seat(ntemp):
    direita = False
    while(ntemp > 12):
        ntemp = ntemp - 12
    if ntemp > 6:
        relativo_1fila = 13 - ntemp
        direita = True
    else:
        relativo_1fila = ntemp
    resp_acento = tipoacento[str(relativo_1fila)]
    seats_between = ((relativo_1fila - 13) + relativo_1fila) * -1
    if direita is True:
        seat_front = n - seats_between
    else:
        seat_front = n + seats_between
    print(str(seat_front) + ' ' + resp_acento)
        
tipoacento = {'1': 'WS', '2': 'MS', '3': 'AS', '4': 'AS', '5': 'MS', '6': 'WS'}
vezestemp = int(input())
if (vezestemp >= 1) and (vezestemp <= 100000):
    vezes = vezestemp
    for i in range(vezes):
        n = int(input())
        if (n <= 108) and (n >= 1):
            ntemp = n
            find_seat(ntemp)
