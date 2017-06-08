alunos = int(input())
lista_alunos = [0] * alunos
for i in range(alunos):
    lista_alunos[i] = i+1
musica = input()
x = 0

while(len(lista_alunos) != 1):
    for i in range(len(musica)):
        nota = musica[i]
        if nota == 'a':
            if x != len(lista_alunos) - 1:
                x = x + 1
            else:
                x = 0
        if nota == 'b':
            if x != len(lista_alunos) - 1:
                azarado = lista_alunos[x]
                lista_alunos.remove(azarado)
                if len(lista_alunos) == 1:
                    break
            else:
                azarado = lista_alunos[x]
                lista_alunos.remove(azarado)
                x = 0
                if len(lista_alunos) == 1:
                    break
print(lista_alunos[0])
        
        
