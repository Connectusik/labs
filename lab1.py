n = input("Введіть число N: ")

if n.isdigit():
    n = int(n)

    print("Число | Квадрат")
    print("---------------")

    for i in range(1 , n+1):
        print(i, "     |", i ** 2)
else:
    if len(n) > 1 and n[0] == '-' and n[1:].isdigit():
        print("Помилка: N < 0")
    else:
        print("Неправильний формат вхідних даних")