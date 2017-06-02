def funcao():
    numero = input('digite um numero menor que 1000: ')
    numero = int(numero)
    c = int(numero/100)
    d = int(numero%100/10)
    u = (numero%100)%10
    if (0 < c != 1):
        ctermo = 'centenas'
    else:
        ctermo = 'centena'
    if (0 < d != 1):
        dtermo = 'dezenas'
    else:
        dtermo = 'dezena'
    if (0 < u != 1):
        utermo = 'unidades'
    else:
        utermo = 'unidade'
        
    if (c != 0):
        print(str(c) + ' ' + ctermo)
    if (d != 0):
        print(str(d) + ' ' + dtermo)
    if (u != 0):
        print(str(u) + ' ' + utermo)

while(1):
    funcao()
