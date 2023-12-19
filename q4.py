def decomposicao(valor):
    notas =  [100, 50, 20, 10, 5, 2, 1]
    qtn_notas = [0, 0, 0, 0, 0, 0, 0]

    print(f'Valor: {valor}')

    for i in range(len(notas)):
        qtn_notas[i] = valor // notas[i]
        valor %= notas[i]
    for i in range(len(notas)):
        if qtn_notas[i] >= 0:
            print(f'{qtn_notas[i]} nota(s) de {notas[i]}')

entrada = int(input('Informe um numero para a decomposição: '))

decomposicao(entrada)