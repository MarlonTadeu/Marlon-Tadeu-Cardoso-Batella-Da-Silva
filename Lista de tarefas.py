tarefas = []

for i in range(5):
    tarefa = input("Digite uma tarefa: ")
    tarefas.append(tarefa)

for i in range(len(tarefas)):
    print(i + 1, "-", tarefas[i])