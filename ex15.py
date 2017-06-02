def caixa():
    valor = input('digite o valor a ser sacado: ')
    valor = int(valor)
    c = valor/100
    c = int(c)
    print(c)
    d = (valor%100)/10
    d = int(d)
    print(d)
    u = (valor%100)%10
    u = int(u)
    print(u)

    if (c != 0):
        print('cem: ' + str(c))
    if (d != 0):
        if (d >= 5):
            print('cinquenta: 1')
            dez = int(d) - 5
            if (dez != 0):
                print('dezenas: ' + str(dez))
        else:
            print('dezenas: ' + str(d))


    if (u != 0):
        if (u >= 5):
            print('cinco: 1')
            umreal = u - 5
            if (umreal != 0):
                print('um real: ' + str(umreal))
        else:
            print('um real: ' + str(u))


while(1):
    caixa()
