
def pedirvalores():
  valores = [0,0,0]
  tt = 0
  for i in range(3):
      valores[i] = int(input('digite o valor ' + str(i) + ' :'));
      if (valores[i] > 0) & (valores[i] < 10):
          tt = tt + 1
          
  print(valores);
  print(tt);
  
  


pedirvalores();



