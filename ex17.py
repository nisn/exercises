def func():
    paisA = int(input('digite a pop1: '))
    taxaA = float(input('taxa de crescimento da pop1: '))
    paisB = int(input('digite a pop2: '))
    taxaB = float(input('taxa de crescimento da pop2: '))
    anos = 0
    while(paisA < paisB):
        paisA = paisA + paisA*(taxaA/100)
        paisB = paisB + paisB*(taxaB/100)
        anos = anos + 1
        print(int(paisA), int(paisB))
    print(anos)


func()
