# Questão A:
def contagem1(numero):
    if numero == 0:
        print('Fim da contagem!')
    else:
        print(numero)
        contagem1(numero - 1)

numero = int(input('Informe um numero para a contagem: '))

contagem1(numero)

# Questão B:
def contagem2(numero):
    for v in range(numero):
        print(numero)
        numero -= 1
    print('Fim da contagem!')

numero_ = int(input('Informe um numero para a contagem: '))

contagem2(numero_)