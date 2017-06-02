def verificanum(j):
#    print('verificando')
    primo = False
    for x in range(j):
        if x > 1:
            if (j % x == 0):
                primo = True
    if primo is False:
        resposta.append(str(j))

        
resposta = []   
m = input()
m = int(m)
for i in range(m):
    if i > 1:
        verificanum(i)
print(' '.join(resposta))
