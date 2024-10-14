"""
Модуль для малювання сегментів фракталу Коха.
Цей модуль містить функцію для рекурсивного малювання
сегментів кривої Коха.
"""

def draw_koch_segment(t, length, level):
    """
    Малює один сегмент кривої Коха за допомогою turtle.
    
    Аргументи:
    - t (turtle.Turtle): Об'єкт turtle для малювання.
    - length (float): Довжина сегменту.
    - level (int): Рівень рекурсії.
    """
    if level == 0:
        t.forward(length)
    else:
        length /= 3
        for angle in [60, -120, 60]:
            draw_koch_segment(t, length, level - 1)
            t.left(angle)
        draw_koch_segment(t, length, level - 1)
