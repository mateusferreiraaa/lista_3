# Definição Variavis:
soma = 0
qnt = 0

# Definição Codigos:
while True:
    entrada = int(input('Escreva qualquer numero, ou "0" para encerrar: '))

    if entrada == 0:
        break
    else:
        soma += entrada
        qnt += 1

if qnt == 0:
    print('Nenhum Numero adicionado!')
else:
    md = soma / qnt
    print(f'\nVocê digitou {qnt} números.')
    print(f'A soma de todos os Númrtos é igual a {soma}.')
    print(f'A media grel é igual a {md}.')