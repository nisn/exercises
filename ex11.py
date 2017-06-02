def triangulo():
    lado1 = int(input('Ladto 1: '))
    lado2 = int(input('Lado 2: '))
    lado3 = int(input('Lado 3: '))
    if ((lado1+lado2)>lado3) or ((lado1+lado3)>lado2) or ((lado2+lado3)>lado1):
        print('Triangulo')
    else:
        print('Nao')
    if (lado1 == lado2 == lado3):
        print('escaleno')
    if (lado1 == lado2 != lado3) or (lado1 != lado2 == lado3) or (lado3 == lado1 != lado2):
        print('isosceles')
        

while(1):
    triangulo()
