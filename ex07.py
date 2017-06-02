gabarito = ['b', 'c', 'a', 'e', 'd', 'a', 'b']
quant = 0
g_aluno = [0, 0, 0, 0, 0, 0, 0]
nomes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
notas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
media = 0


def principal():
    quant = input('Quantos alunos (< 10) ? ')
    quant = int(quant)
    for i in range(quant):
        nomes[i] = input('Nome do aluno ' + str(i + 1) + ': ')
        for x in range(len(gabarito)):
            g_aluno[x] = input('Resposta questao ' + str(x + 1) + ' : ')
        print(nomes[i])
      
    return


principal()
