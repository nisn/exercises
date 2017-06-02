def upload():
    L = input()
    N = input()
    if (1 <= int(N) <= 1000):
        N = int(N)
        while (N > 0):
            W, H = input().split(' ')
            W = int(W)
            H = int(H)
            L = int(L)
            if (W < L) or (H < L):
                print('UPLOAD ANOTHER')
            else:
                if (W == H):
                    print('ACCEPTED')
                else:
                    print('CROP IT')
            N = N - 1
upload()
