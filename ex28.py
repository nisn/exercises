l , r , k = input().split(' ')
l = int(l)
r = int(r)
k = int(k)
ltemp = l
contador = 0
while(ltemp <= r):
    if (ltemp%k == 0):
        contador = contador + 1
    ltemp = ltemp + 1
print(contador)
