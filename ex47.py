word_length = int(input())
word1 = input()
word2 = input()
achou = True
achou1 = False
achou2 = False
for i in range(word_length):
    if achou is True:
        achou = False
        for ii in range(len(word1)):
            if word1[i] == word2[ii]:
                if str(word1).count(word1[i]) == str(word2).count(word1[i]):
                    achou = True
if achou is True:
    achou1 = True
else:
    achou1 = False

achou = True
for i in range(word_length):
    if achou is True:
        achou = False
        for ii in range(len(word2)):
            if word2[i] == word1[ii]:
                if str(word1).count(word2[i]) == str(word2).count(word2[i]):
                    achou = True

if achou is True:
    achou2 = True
else:
    achou2 = False

if achou1 and achou2 is True:
    print('YES')
else:
    print('NO')
    
