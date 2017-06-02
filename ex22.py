def fact():
    num = input('opjkjkk')
    try:
        int(num)
    except ValueError:
        print('erro, numero invalido')
        return
    num = int(num)
    if (num < 0) or (num > 16):
        print('numero neg ou maior que 16')
        return
    temp = num
    for i in range(int(num)):
        if i != 0:
            temp = temp*(num-i)
    print(temp)


while 1:
    fact()
