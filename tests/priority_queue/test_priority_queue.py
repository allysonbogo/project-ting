from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    high_priority = {"nome_do_arquivo": "arquivo_1.txt", "qtd_linhas": 3}
    regular_priority = {"nome_do_arquivo": "arquivo_3.txt", "qtd_linhas": 6}

    priority_queue.enqueue(regular_priority)
    priority_queue.enqueue(high_priority)

    assert len(priority_queue) == 2

    assert priority_queue.search(0) == high_priority
    assert priority_queue.search(1) == regular_priority
    try:
        priority_queue.search(2)
    except IndexError as error:
        assert str(error) == "Índice Inválido ou Inexistente"

    assert priority_queue.dequeue() == high_priority
    assert priority_queue.dequeue() == regular_priority
    try:
        priority_queue.dequeue()
    except Exception as error:
        assert str(error) == "Queue is empty"

    assert len(priority_queue) == 0
