test_cases = int(input())
for t in range(test_cases):
    case = int(input())
    list_mult = []
    sum_list = 0
    inc_sum = 0
    for i in range(case):
        if (i % 3 == 0) or (i % 5 == 0):
            list_mult.append(str(i))
            sum_list = sum_list + int(list_mult[inc_sum])
            inc_sum = inc_sum + 1
 #   for ii in range(len(list_mult)):
 #       sum_list = sum_list + int(list_mult[ii])
    print(sum_list)
    
