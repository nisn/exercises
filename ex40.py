k = int(input())
sequence = input()
dif_coins = ''
dif_coins_num = 0
new_search = True
achou = 0
inicio = 0
def pesquisa():
    global inicio
    global achou
    new_search = True
    for i in range(inicio, len(sequence)):
        if new_search is True:
            dif_coins = sequence[i]
            dif_coins_num = 1
            new_search = False
        else:
            if dif_coins.find(sequence[i]) == -1:
                dif_coins = dif_coins + sequence[i]
                dif_coins_num = dif_coins_num + 1
#                print(dif_coins)
#                print(dif_coins_num)
            else:
                dif_coins = dif_coins + sequence[i]
#                print(dif_coins)
#                print(dif_coins_num)
            if dif_coins_num == k:
                achou = achou + 1
#                print(achou)
            if (dif_coins_num > k) and (k != 1):
                break
                
    inicio = inicio + 1
    
while (inicio != len(sequence) - 1):
    if (k <= 26) and (k >= 1) and (len(sequence) >= 1) and (len(sequence) <= 5000):
        pesquisa()
if k == 1:
    print(len(sequence))
else:
    print(achou)
