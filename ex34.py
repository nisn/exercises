def check_primo(num):
    flag_primo = True
    for i in range(num-1, 1, -1):
        if (num % i == 0):
            flag_primo = False
    return flag_primo


def check_maior_menor(ascii_real, maior, menor):
    if abs(ascii_real - menor) == abs(ascii_real - maior):
        return('menor')
    if abs(ascii_real - menor) > abs(ascii_real - maior):
        return('maior')
    else:
        return('menor')

    
num_vezes = int(input())
if (num_vezes >= 1) and (num_vezes <= 100):
    for w in range(num_vezes):
        num_letras = int(input())
        letras = input()
        if (len(letras) >= 1) and (len(letras) <= 500):
            final_ascii = 0
            frase_final = ''
            for i in range(num_letras):
                ascii_equi = ord(letras[i])
        #        print(ascii_equi)
                temp_ascii_menor = ascii_equi
                while check_primo(temp_ascii_menor) is False:
                    temp_ascii_menor = temp_ascii_menor - 1
                if temp_ascii_menor == ascii_equi:
                    final_ascii = ascii_equi
                    maior_ou_menor = 'primo'
                else:
                    temp_ascii_maior = ascii_equi
                    while check_primo(temp_ascii_maior) is False:
                        temp_ascii_maior = temp_ascii_maior + 1
                    maior_ou_menor = check_maior_menor(ascii_equi, temp_ascii_maior, temp_ascii_menor)
        #        print(maior_ou_menor)
                if maior_ou_menor != 'primo':
                    if maior_ou_menor == 'menor':
                        final_ascii = temp_ascii_menor
                    else:
                        final_ascii = temp_ascii_maior
        #        print(final_ascii)
                frase_final = frase_final +
                chr(final_ascii)
            print(frase_final)
            
