""" verifica numero primo """


def primo():  # funcao primo
    primoflag = 'unset'
    primolist = []
    num = int(input('digite um numero: '))
    for i in range(num):
        if (i > 0) and (i != num-1):
            if num % (num-i) == 0:
                primolist.append(num-i)
                primoflag = 'nao'

    if primoflag == 'unset':
        print('numero primo!')
    else:
        print('numero divisivel por: ' + str(primolist))


while(1):
    primo()
