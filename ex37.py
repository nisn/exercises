# find how many times can produce string 'hackerearth' for given input
len_string = input()
the_string = input()
letters = [0] * 7
x = 1
possivel = 0
# h=0/a=1/c=2/k=3/e=4/r=5/t=6
for i in range(int(len_string)):
    if the_string[i] == 'h':
        letters[0] = letters[0] + 1
    if the_string[i] == 'a':
        letters[1] = letters[1] + 1
    if the_string[i] == 'c':
        letters[2] = letters[2] + 1
    if the_string[i] == 'k':
        letters[3] = letters[3] + 1
    if the_string[i] == 'e':
        letters[4] = letters[4] + 1
    if the_string[i] == 'r':
        letters[5] = letters[5] + 1
    if the_string[i] == 't':
        letters[6] = letters[6] + 1
# print(letters)
while (letters[0] >= 2*x) and (letters[1] >= 2*x) and (letters[2] >= x) and (letters[3] >= x) and (letters[4] >= 2*x) and (letters[5] >= 2*x) and (letters[6] >= x):
    x = x + 1
    possivel = possivel + 1
print(possivel)
