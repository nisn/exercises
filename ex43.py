num_numeros = int(input())
lista_num = str(input()).split(' ')
tmp = str(input()).split(' ')
S = tmp[0]
E = tmp[1]
x = int(S) - 1
tentativas = 0
achou = False

if S == E:
    achou = True
else:
    while(tentativas < num_numeros):
        if lista_num[x] == E:
            achou = True
            break
        else:
            x = int(lista_num[x]) - 1
            tentativas = tentativas + 1
    
if achou is True:
    print('Yes')
else:
    print('No')

