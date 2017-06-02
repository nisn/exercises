def main():
    nome = []
    idade = []
    maioridade = 0
    maiorindex = 0
    for contador in range(3):
        nome.append(input('digite o nome ' + str(contador) + ': ' ))
        idade.append(input('digite o idade ' + str(contador) + ': ' ))
        if int(idade[contador]) > maioridade:
            maiorindex = contador
    print(nome)
    print(maiorindex)
    print('maior: ' + nome[maiorindex])
    
main()        
