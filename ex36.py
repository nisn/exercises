numero = input()
tamanho_n = len(numero)
registro = [0] * 10
for i in range(tamanho_n):
    temp_n = int(numero[i])
    registro[temp_n] = registro[temp_n] + 1
for i in range(10):
    print(str(i) + ' ' + str(registro[i]))
    
    
