v = [0,0,0,0,0]
soma = 0;
media = 0;
div5 = 0;
nulos = 0;
somapares = 0;
for i in range(5):
    v[i] = input('digite o valor ' + str(i) + ' :')
    soma = int(v[i]) + soma;
media = soma/5;
for i in range(5):
    v[i] = int(v[i])
    if (v[i]%5 == 0) & (v[i] != 0):
        div5 = div5 + 1
    if v[i] == 0:
        nulos = nulos + 1
    if v[i]%2 == 0:
        somapares = v[i] + somapares
print('divide por 5: ' + str(div5))
print('soma :' + str(soma))
print('media :' + str(media))
print('soma dos pares :' + str(somapares))
print('nulos :' + str(nulos))
