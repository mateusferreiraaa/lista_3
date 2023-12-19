# Questão A:
def numeros_1a100():
    for i in range(1, 101):
        print(i)

numeros_1a100()

# Questão B:
def numeros_50a100():
    for i in range(50, 101, 2):
        print(i)

# Questão C:
c = 10

while True:
    if c > 0:
        print(c)
        if c == 1:
            print('Fogo!')
        c = c - 1
    elif c == 0:
        break

# Questão D:
entra = int(input('Informe um Numero: '))
entra2 = input('Digite "P" para os numeros Pares, ou "I" para os Ínpares: ')

if entra2 == 'P' or entra2 == 'p':
    entra = entra + 1
    d = list(range(2, entra, 2))
    print(d)
elif entra2 == 'I' or entra2 == 'i':
    entra = entra + 1
    d = list(range(1, entra, 2))
    print(d)