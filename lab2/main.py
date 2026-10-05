import os
from lab2 import replace_with_backup

path = input("Введіть шлях до файлу: ")
old = input("Що замінити: ")
new = input("На що замінити: ")

if not os.path.exists(path):
    print("Помилка: такого файлу не існує")

elif not os.path.isfile(path):
    print("Помилка: вказаний шлях не є файлом")

elif not os.access(path, os.R_OK):
    print("Помилка: файл неможливо прочитати")

elif not os.access(path, os.W_OK):
    print("Помилка: файл неможливо змінити")

elif old == "":
    print("Помилка: рядок для заміни не може бути порожнім")

else:
    count = replace_with_backup(path, old, new)

    print()
    print("Файл успішно оброблено")
    print("Кількість замін:", count)
    print("Резервна копія:", path + ".bak")