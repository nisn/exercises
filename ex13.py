def dataformat():
    data = input('digita data no formato dd/mm/aaaa : ')
    dia = data[0] + data[1]
    mes = data[3] + data[4]
    ano = data[6] + data[7] + data[8] + data[9]
    print(dia)
    print(mes)
    print(ano)
    if (data[2] and data[5] == '/'):
        if (0 < int(dia) <= 31) & (0 < int(mes) <= 12) & (0000 < int(ano) <= 3000):
            print('dia correto')
        else:
            print('formato invalido!')
    else:
        print('falta barra')

        
while(1):
    dataformat()
