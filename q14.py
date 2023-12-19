def referencia(paassagem1):
    print(f'Valor no inicio: {paassagem1}')
    paassagem1 = 77
    print(f'Valor depois: {paassagem1}')

x = 7
referencia(x)
print(f'Valor fora da função: {x}')

def valor(paassagem2):
    paassagem2 = y
    print(f'Valor no inicio: {paassagem2}')
    paassagem2 = 77
    print(f'Valor depois: {paassagem2}')

y = 7
valor(y)
print(f'Valor fora da função: {y}')