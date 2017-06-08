num_badwords = int(input())
badwords = [0] * int(num_badwords)
for i in range(num_badwords):
    badwords[i] = input()
num_words = int(input())
words = str(input())
words_cortadas = words.split(' ')
achou = []

for w in range(num_badwords):
    badword_find = badwords[w]
    for y in range(len(words_cortadas)):
        if badword_find == words_cortadas[y]:
            achou.append(badword_find)
words_cortadas_copy = words_cortadas[:]

for h in range(len(achou)):
    achou_tmp = achou[h]
    for j in range(len(words_cortadas)):
        if words_cortadas[j] == achou_tmp:
            if words_cortadas_copy.count(achou_tmp) > 0:
                words_cortadas_copy.remove(achou_tmp)

first_letter_final = ''
for g in range(len(words_cortadas_copy)):
    first_letter_tmp = words_cortadas_copy[g]
    first_letter_tmp = first_letter_tmp[0]
    first_letter_final = first_letter_final + first_letter_tmp.upper()
    if g != len(words_cortadas_copy) - 1:
        first_letter_final = first_letter_final + '.'
print(first_letter_final)
