# little jhool and psychic powers
msg = input()
x = 0
lucky = False
for i in range(len(msg)):
    if i != len(msg) - 1:
        if x != 5:
            if i != len(msg) - 1:
                if (msg[i] == msg[i+1]):
                    x = x + 1
                else:
                    x = 0
        else:
            if (msg[i] != msg[i+1]):
                lucky = True
                break
    else:
        if x == 5:
            lucky = True
            
if lucky is False:
    print('Good luck!')
else:
    print('Sorry, sorry!')
    
    
