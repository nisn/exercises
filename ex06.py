times = ['vasco', 'botafogo', 'america', 'palmeiras']
for i in range(len(times)):
    x = 0
    while x < len(times):
        if (i != x):
            print(times[i] + ' X ' + times[x])
        x = x + 1
