"""
Основний модуль програми для малювання фракталу сніжинки Коха.
Цей модуль ініціалізує вікно, створює об'єкт turtle
та запускає процес малювання.
"""

import turtle
from draw_snowflake import draw_snowflake

def main():
    """
    Основна функція програми. Підготовляє вікно,
    ініціалізує turtle і починає малювання сніжинки Коха.
    """
    level = int(input("Введіть рівень рекурсії (рекомендовано 0-5): "))

    screen = turtle.Screen()
    screen.title("Сніжинка Коха")
    screen.setup(width=800, height=600)

    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість малювання
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    length = 400
    draw_snowflake(t, length, level)

    turtle.done()

if __name__ == "__main__":
    main()
