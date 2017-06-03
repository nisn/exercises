# min-max hackerearth
def maior_menor():
    global menor
    global maior
    global num_numeros
    global numeros
    for i in range(num_numeros):
        if i == 0:
            menor = int(numeros[i])
            maior = int(numeros[i])
        else:
            if int(numeros[i]) < menor:
                menor = int(numeros[i])
            if int(numeros[i]) > maior:
                maior = int(numeros[i])

                
num_numeros = int(input())
numeros = str(input()).split(' ')
menor = 0
maior = 0
maior_menor()

achou = True
for w in range(menor+1, maior, 1):
    if achou is True:
        achou = False
        for i in range(num_numeros):
            if int(numeros[i]) == int(w):
                achou = True
if achou is True:
    print('YES')
else:
    print('NO')
    
