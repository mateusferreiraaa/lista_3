# Questão A:
def multiplicar(a, b):
    resultado = 0

    for i in range(b):
        resultado += a
    
    return resultado

n1 = int(input('Digite um Numero: '))
n2 = int(input('Digite um Numero: '))

resultado = multiplicar(n1, n2)

print(f'A multiplicação é igual a {resultado}!')

# Questão B:
def dividir_resto(a, b):
    resultado = 0
    resto = a
    while resto >= b:
        resto -= b
        resultado += 1
    
    return resultado, resto

nu1 = int(input('Informe um Numero: '))
nu2 = int(input('Informe um Numero: '))

divisao, resto = dividir_resto(nu1, nu2)

print(f'A divisão é igual a {divisao}, restando {resto}!')