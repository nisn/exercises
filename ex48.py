# roy and leds
def led_list(tempo_led):
    the_list = []
    ligado = False
    contador = 1
    for i in range(tempo):
        if ligado is False:
            the_list.append(0)
        else:
            the_list.append(1)  
        if contador < tempo_led:
            contador = contador + 1
        else:
            contador = 1
            ligado = not ligado
    return(the_list)


tempo, r, g, b = str(input()).split(' ')
tempo = int(tempo)
r_list = led_list(int(r))
g_list = led_list(int(g))
b_list = led_list(int(b))

output_sum = [0] * 8
for w in range(tempo):
    if (r_list[w] == 1) and (g_list[w] == 0) and (b_list[w] == 0):
        output_sum[0] = output_sum[0] + 1
    if (r_list[w] == 0) and (g_list[w] == 1) and (b_list[w] == 0):
        output_sum[1] = output_sum[1] + 1
    if (r_list[w] == 0) and (g_list[w] == 0) and (b_list[w] == 1):
        output_sum[2] = output_sum[2] + 1
    if (r_list[w] == 1) and (g_list[w] == 1) and (b_list[w] == 0):
        output_sum[3] = output_sum[3] + 1
    if (r_list[w] == 0) and (g_list[w] == 1) and (b_list[w] == 1):
        output_sum[4] = output_sum[4] + 1
    if (r_list[w] == 1) and (g_list[w] == 0) and (b_list[w] == 1):
        output_sum[5] = output_sum[5] + 1
    if (r_list[w] == 1) and (g_list[w] == 1) and (b_list[w] == 1):
        output_sum[6] = output_sum[6] + 1
    if (r_list[w] == 0) and (g_list[w] == 0) and (b_list[w] == 0):
        output_sum[7] = output_sum[7] + 1
final_list = ''
for j in range(len(output_sum)):
    final_list = final_list + str(output_sum[j]) + ' '
final_list = final_list.rstrip(' ')
print(final_list)

    
