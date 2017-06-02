num_numeros = int(input())
numeros = input()
numeros = str(numeros)
w = numeros.split(' ')
resp = 1
for i in range(num_numeros):
    resp = (resp * int(w[i])) % (pow(10,9) + 7)
print(resp)
