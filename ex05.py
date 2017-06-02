vetor = [7,2,9,1,6,4,3,8,5]
print(vetor)
for i in range(len(vetor)):
    x = i+1;
    while x < len(vetor):
        if vetor[i] > vetor[x]:
            tt = vetor[i]
            vetor[i] = vetor[x]
            vetor[x] = tt
        x = x + 1
print(vetor)
