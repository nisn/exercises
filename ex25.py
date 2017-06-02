def separador():
    g1 = 0
    g2 = 0
    g3 = 0
    g4 = 0
    entrada = 0
    finaliza = False
    while(not finaliza):
        entrada = int(input('Digite um numero ou "-1" para sair: '))
        if entrada < 0:
            finaliza = True
        else:
            if (entrada <= 25):
                g1 = g1 + 1
            if (entrada > 25) and (entrada <= 50):
                g2 = g2 + 1
            if (entrada > 50) and (entrada <= 75):
                g3 = g3 + 1
            if (entrada > 75) and (entrada <= 100): g4 = g4 + 1 
    print(g1, g2, g3, g4)

separador()


