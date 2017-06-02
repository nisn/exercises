m = []
i = 1
tt = 0
maior = 0
menor = 'n'
while (tt != 's'):
    tt = input('numero ' + str(i) + ' : ')
    m.append(tt)

    if (tt != 's'):
        if (int(tt) > int(maior)):
            maior = tt
        if menor == 'n':
            menor = tt
        else:
            if int(tt) < int(menor):
                menor = tt
    print(m)
m.remove('s')
print(m)
print(maior)
print(menor)
