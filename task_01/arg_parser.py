"""
Модуль для парсингу аргументів командного рядка для програми копіювання та сортування файлів.

Аргументи:
1. -s/--source (обов'язковий): Шлях до вихідної директорії.
2. -d/--dest (необов'язковий, за замовчуванням 'dist'): Шлях до цільової директорії.

Модуль містить одну функцію `parse_args()`, яка відповідає за обробку цих аргументів.
"""

import argparse
from pathlib import Path

def parse_args() -> argparse.Namespace:
    """
    Парсить аргументи командного рядка для програми.

    Аргументи:
    - -s/--source (Path, обов'язковий): Шлях до вихідної директорії.
    - -d/--dest (Path, необов'язковий): Шлях до директорії
    призначення. Якщо не передано, буде використано "dist".

    Повертає:
    - argparse.Namespace: Об'єкт з переданими аргументами.
    """
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання і сортування файлів.")
    parser.add_argument("-s", "--source", type=Path, required=True, help="Шлях до вихідної директорії")
    parser.add_argument("-d", "--dest", type=Path, default=Path("dist"), help="Шлях до директорії призначення (за замовчуванням dist)")

    return parser.parse_args()
