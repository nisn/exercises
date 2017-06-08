num_cases = int(input())
x = 0


def produto_alfabet(word_in):
    alfab_valores = {}
    y = 1
    mult_final = 1
    for j in range(ord('a'), ord('z')+1):
        alfab_valores[chr(j)] = y
        y = y + 1
    for h in range(len(word_in)):
        mult_final = mult_final * int(alfab_valores[word_in[h]])
    print(mult_final)

    
while (x < num_cases):
    word_in = input()
    word_invert = ''
    for i in range(len(word_in), 0, -1):
        word_invert = word_invert + word_in[i-1]
    if word_in == word_invert:
        print('Palindrome')
    else:
        produto_alfabet(word_in)
    x = x + 1
