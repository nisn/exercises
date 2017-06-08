string_len = int(input())
string = input()
w_to_vv = str(string).replace('w', 'vv')
vv_to_w = str(w_to_vv).replace('vv', 'w')
print(len(vv_to_w), end=' ')
print(len(w_to_vv))

