"""
Modulo que implementa um gerenciador de tarefas
"""


lista_de_tarefas: list[dict[str]] = [
    {"prioridade": True, "tarefa": "Estudar Python"},
    {"prioridade": False, "tarefa": "Tomar banho"},
    {"prioridade": False, "tarefa": "Assistir série"},
]


def adicionar_tarefa(prioridade: bool, tarefa: str):
    """
    Adiciona uma tarefa na lista de tarefas
    Lança exceções caso a prioridade seja inválida ou a tarefa já exista

    Args:
        prioridade (bool): True se a tarefa tem prioridade alta, False caso contrário
        tarefa (str): string que representa a tarefa
    """
    # TODO: coloque o código aqui para adicionar um tarefa na lista
    # Caso a prioridade não seja True ou False, levante uma exceção
    # do tipo ValueError com a mensagem "Prioridade inválida"
    # Caso a tarefa já exista na lista, levante uma exceção do tipo ValueError
    # com a mensagem "Tarefa já existe"
    if prioridade not in [True, False]:
        raise ValueError("Prioridade inválida")

    for item in lista_de_tarefas:
        if item["tarefa"] == tarefa:
            raise ValueError("Tarefa já existe")

    nova_tarefa = {"prioridade": prioridade, "tarefa": tarefa}
    lista_de_tarefas.append(nova_tarefa)



def remove_tarefas(índices: tuple[int]):
    """
    Remove várias tarefas da lista de tarefas de uma vez, dado uma tupla de índices
    Lança exceções caso a tarefa não exista

    Args:
        índices (tuple[int]): tupla de inteiros que representam os índices das tarefas
                            que devem ser removidas da lista.
    """
    # TODO: coloque o código aqui para remover um tarefa na lista
    # Caso a tarefa não exista na lista, levante uma exceção do tipo ValueError
    # com a mensagem "Tarefa não existe"
    c = 0
    for i in índices:
        del lista_de_tarefas[i - c]    
        c = c + 1

    if not índices:
        raise ValueError("Tarefa não existe")


def encontra_tarefa(tarefa: str) -> int:
    """
    Encontra o índice de uma tarefa na lista de tarefas
    Lança exceções caso a tarefa não exista

    Args:
        tarefa (str): string que representa a tarefa
    """
    # TODO: coloque o código aqui para encontrar um tarefa na lista
    # Caso a tarefa não exista na lista, levante uma exceção do tipo ValueError
    # com a mensagem "Tarefa não existe"
    for i in lista_de_tarefas:
        if tarefa == i["tarefa"]:
            return lista_de_tarefas.index(i)
    
    raise ValueError("Tarefa não existe")


def ordena_por_prioridade():
    """
    Ordena a lista de tarefas por prioridade com as tarefas prioritárias no
    início da lista, seguidas pelas tarefas não prioritárias.
    As tarefas prioritárias devem ser ordenadas por ordem alfabética e as
    tarefas não prioritárias devem ser ordenadas por ordem alfabética.
    """
    # TODO: coloque o código aqui para ordenar a lista de tarefas por prioridade
    # com as tarefas prioritárias no início da lista, seguidas pelas tarefas
    # não prioritárias.
    # As tarefas prioritárias devem ser ordenadas por ordem alfabética e as
    # tarefas não prioritárias devem ser ordenadas por ordem alfabética.
    lista_de_tarefas.sort(key=lambda tarefa: (not tarefa["prioridade"], tarefa["tarefa"]))

def get_lista_de_tarefas():
    """
    Retorna somente o texto das tarefas da lista de tarefas
    """
    texts = []
    for tarefa in lista_de_tarefas:
        texto = tarefa["tarefa"]
        prioridade = tarefa["prioridade"]
        texts.append(f"{'*' if prioridade else ''} {texto}")
    return tuple(texts)
