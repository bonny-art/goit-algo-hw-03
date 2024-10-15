"""
Модуль hanoi.py

Цей модуль містить функцію hanoi, яка рекурсивно переміщує диски
з одного стрижня на інший, використовуючи допоміжний стрижень.
"""

def hanoi(n, source, target, auxiliary, state):
    """
    Рекурсивно переміщує n дисків з одного стрижня на інший, використовуючи допоміжний стрижень.

    Аргументи:
    - n (int): Кількість дисків.
    - source (str): Назва початкового стрижня.
    - target (str): Назва цільового стрижня.
    - auxiliary (str): Назва допоміжного стрижня.
    - state (dict): Словник для відстеження стану стрижнів.
    """
    if n == 1:
        disk = state[source].pop()
        state[target].append(disk)

        print(f"\nПеремістити диск {disk} з {source} на {target}.")
        print("Проміжний стан:", state)

    else:
        hanoi(n - 1, source, auxiliary, target, state)
        disk = state[source].pop()
        state[target].append(disk)

        print(f"\nПеремістити диск {disk} з {source} на {target}.")
        print("Проміжний стан:", state)

        hanoi(n - 1, auxiliary, target, source, state)
