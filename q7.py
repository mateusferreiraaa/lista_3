def verifica_parenteses(expressao):
    pilha = []

    for veri in expressao:
        if veri == '(':
            pilha.append(veri)
        elif veri == ')':
            if not pilha:
                return "Erro: parênteses fechados sem terem sido abertos."
            pilha.pop()

    if not pilha:
        return "OK"
    else:
        return "Erro: parênteses abertos sem terem sido fechados."


expressao = input("Digite a expressão com parênteses: ")

resultado = verifica_parenteses(expressao)
print(resultado)