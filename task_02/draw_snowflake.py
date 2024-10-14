"""
Модуль для малювання фрактала сніжинки Коха.
Цей модуль містить функцію для малювання сніжинки
з використанням трьох сегментів.
"""

from draw_koch_segment import draw_koch_segment

def draw_snowflake(t, length, level):
    """
    Малює фрактал сніжинки Коха з трьох сегментів.
    
    Аргументи:
    - t (turtle.Turtle): Об'єкт turtle для малювання.
    - length (float): Довжина сторони сніжинки.
    - level (int): Рівень рекурсії.
    """
    for _ in range(3):
        draw_koch_segment(t, length, level)
        t.right(120)
