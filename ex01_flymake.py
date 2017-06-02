
def pedirnumero():
    numero = input('digite um numero: ');
    if (int(numero)%2 == 1):
        print('impar, digite outro numero.');
        pedirnumero();
        
    else:
        pares_ate_zero(numero)
        print('fim da outra funcao')

        
def pares_ate_zero(num):
    num = int(num)
    while num >= 0:
        print(num)
        num = num - 2;
    print('acabou');

while (1):
    pedirnumero();



