def func():
    vogal = ['a', 'e', 'i', 'o', 'u']
    letra = input('digite uma letra: ')
    for i in range(5):
        if (letra == vogal[i]):
            print('vogal')
            return
    print('consoante')

    
while(1):
    func()
