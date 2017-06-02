diasemana = ['segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']
def diadasemana():
    i = int(input('digite o dia (1 ate 7) : '))
    if (i >= 1) & (i <= 7):
        print(diasemana[i-1])
    else:
        print('numero invalido')
        diadasemana()

while(1):
    diadasemana()
