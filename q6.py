def contem_item(lista, item):
    return item in lista

def combinar_listas(lista1, lista2):
    resultado = []
    
    for item in lista1:
        if not contem_item(resultado, item):
            resultado.append(item)
    
    for item in lista2:
        if not contem_item(resultado, item):
            resultado.append(item)
    
    return resultado

lista1 = [1, 2, 3, 4]
lista2 = [2, 4, 5, 6]

lista_combinada = combinar_listas(lista1, lista2)

print('Lista 1:', lista1)
print('Lista 2:', lista2)
print('Lista combinada sem elementos repetidos:', lista_combinada)