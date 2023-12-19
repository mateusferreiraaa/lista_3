lista_de_tarefas = []

while True:
    def adicionar_tarefa(entrada):
        lista_de_tarefas.append(entrada)
        print(f'{entrada} foi adicionado a lista!')

    def exibir_tarefas():
        numero = 1
        print('\nAqui esta sua Lista:')
        for tarefa in lista_de_tarefas:
            print(f'{numero}. {tarefa}')
            numero += 1


    tarefa = input('Informe a tarefa a ser listada, ou "0" para finalzar: ')

    if tarefa == '0':
        exibir_tarefas()
    else:
         adicionar_tarefa(tarefa)