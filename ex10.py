def media():
    conceito = [0,0]
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = ((nota1+nota2)/2)
    print('media: ' + str(media))
    if (media >= 9) & (media <= 10):
        conceito[0] = '- Aprovado'
        conceito[1] = 'A'
    if (media >= 7.5) & (media < 9):
        conceito[0] = 'Aprovado'
        conceito[1] = 'B'
    if (media >= 6) & (media < 7.5):
        conceito[0] = 'Aprovado'
        conceito[1] = 'C'
    if (media >= 4) & (media < 6):
        conceito[0] = 'Reprovado'
        conceito[1] = 'D'
    if (media >= 0) & (media < 4):
        conceito[0] = 'Reprovado'
        conceito[1] = 'E'
    print(conceito[0] + '.\n- Conceito: ' + conceito[1])

while(1):
    media()
