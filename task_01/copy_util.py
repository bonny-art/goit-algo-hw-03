"""
Модуль для рекурсивного копіювання файлів з сортуванням за розширенням.

Функціонал:
1. Копіює файли з вихідної директорії у цільову директорію.
2. Створює піддиректорії в цільовій директорії на основі розширення файлів.
3. Якщо файл з таким ім'ям вже існує, додає до імені файлу
суфікс з інкрементом, щоб уникнути перезапису.

Модуль містить функцію `copy_and_sort_files()`, яка виконує основну логіку копіювання.
"""

import os
import shutil
from typing import Union

def copy_and_sort_files(src_dir: Union[str, os.PathLike], dest_dir: Union[str, os.PathLike]) -> None:
    """
    Рекурсивно копіює файли з вихідної директорії у цільову директорію, сортує їх за розширенням
    та створює піддиректорії на основі розширення файлів.

    Якщо файл з таким іменем вже існує, додається
    інкрементальний суфікс до імені файлу для уникнення перезапису.

    Аргументи:
    - src_dir (str | os.PathLike): Шлях до вихідної директорії.
    - dest_dir (str | os.PathLike): Шлях до цільової директорії.

    Дії:
    - Рекурсивно обходить всі файли і піддиректорії в вихідній директорії.
    - Копіює файли у піддиректорії за розширенням у цільовій директорії.
    - Уникає перезапису файлів шляхом додавання суфіксу до імені файлу.
    """
    try:
        # Проходження по елементах вихідної директорії
        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)

            if os.path.isdir(src_path):
                # Рекурсивне копіювання піддиректорій
                copy_and_sort_files(src_path, dest_dir)

            elif os.path.isfile(src_path):
                # Визначення розширення файлу або присвоєння 'no_extension'
                file_extension = os.path.splitext(item)[1][1:] or 'no_extension'

                # Створення піддиректорії за розширенням
                dest_path = os.path.join(dest_dir, file_extension)
                os.makedirs(dest_path, exist_ok=True)

                # Створення унікального шляху для файлу в цільовій директорії
                dest_file_path = os.path.join(dest_path, item)

                # Якщо файл вже існує, додається суфікс з інкрементом
                counter = 1
                while os.path.exists(dest_file_path):
                    name, ext = os.path.splitext(item)
                    dest_file_path = os.path.join(dest_path, f"{name}_{counter}{ext}")
                    counter += 1

                # Копіювання файлу
                shutil.copy2(src_path, dest_file_path)
                print(f"Копіюємо {src_path} -> {dest_file_path}")

    # Обробка можливих помилок
    except FileNotFoundError as e:
        print(f"Файл або директорія не знайдені: {e}")
    except PermissionError as e:
        print(f"Доступ заборонено, файл може бути зайнятий іншою програмою: {e}")
    except OSError as e:
        print(f"Помилка з файловою системою: {e}")
