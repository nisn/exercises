def func():
    ano = int(input('digite o ano: '))
    if ((ano % 4) == 0) & ((ano % 100) != 0):
        print('bissexto')
    if ((ano % 4) != 0):
        if ((ano % 400) != 0):
            print('nao bissexto')
        if ((ano % 400) == 0):
            print('bissexto')

            
while(1):
    func()
