while True:
    def tabuada(entrada):

        if entrada == 1:
            numero = int(input('Informe qual numero que você quer saber a tabuada: '))
            for a in range(1, 11):
                resultado = numero + a
                print(f'{numero} + {a} = {resultado}')
        elif entrada == 2:
            numero = int(input('Informe qual numero que você quer saber a tabuada: '))
            for s in range(1, 11):
                resultado = numero - s
                print(f'{numero} - {s} = {resultado}')
        elif entrada == 3:
            numero = int(input('Informe qual numero que você quer saber a tabuada: '))
            for d in range(1, 11):
                resultado = numero / d
                print(f'{numero} / {d} = {resultado}')
        elif entrada == 4:
            numero = int(input('Informe qual numero que você quer saber a tabuada: '))
            for m in range(1, 11):
                resultado = numero * m
                print(f'{numero} x {m} = {resultado}')
        elif entrada ==  0:
            print('Você parou o programa!!')
            return False
        else:
            print(f'"{entrada}" é uma opão invalida!')


    print('Precione (1) para Adição, (2) para Subtração, (3) para Divisão, (4) para Multiplicação, ou (0) para Sair.')
    entrada = int(input('Resposta: '))

    tabuada(entrada)

    if entrada == False:
        break