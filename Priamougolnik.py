"""задание2. Реализуйте рекурсивную функцию нарезания прямоугольника с заданными пользователем сторонами a и b
на квадраты с наибольшей возможной на каждом этапе стороной. Выведите длины ребер получаемых квадратов
 и кол-во полученных квадратов"""

a = int(input("введите сторону А "))
b = int(input("введите сторону В "))


def squares(a, b, count = 0):
    if a == 0 or b == 0:
        print("Всего квадратов = ", count)
        return
    if a > b:
        print("Квадрат с ребром ", b)
        squares(a - b, b, count + 1)
    else:
        print("Квадрат с ребром ", a)
        squares(a, b - a, count + 1)

squares(a, b)
