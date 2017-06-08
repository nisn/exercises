vezes = int(input())
for u in range(vezes):
    friend_totalp = str(input()).split(' ')
    prices = []
    sim_ou_nao = False
    for i in range(int(friend_totalp[0])):
        prices.append(str(input()))
    if prices.count(friend_totalp[1]) == 0:
        nova = 0
        for w in range(len(prices)):
            nova = int(prices[w])
            for h in range(w+1, len(prices)):
                nova = nova + int(prices[h])
                if nova == int(friend_totalp[1]):
                    sim_ou_nao = True
    else:
        sim_ou_nao = True
    if sim_ou_nao is True:
        print('YES')
    else:
        print('NO')
        

