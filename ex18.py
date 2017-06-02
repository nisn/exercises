numero = []
numeroorg = ''
for i in range(21):
    if (i != 0):
        numero.append(i)
for i in range(20):
    numeroorg = numeroorg + ' ' + str(numero[i])
print(numeroorg)
