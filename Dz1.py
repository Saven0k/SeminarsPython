a, b, c = int(input("Введите сторону a: ")), int(input("Введите сторону b: ")), int(input("Введите сторону c: "))

if (a > b + c) or (b > a + c) or (c > a + b): print("Такого треугольника не существует")
if (a == b == c): print("Этот треbгольник равносторонний")
if (a == b) or (a == c) or (b == c): print("Этот треугольник равнобедренный")
# Проверка на свое усмотрение
if (a ** 2 == b ** 2 + c ** 2) or (c ** 2 == a ** 2 + b ** 2) or (b ** 2 == a ** 2 + c ** 2):
    print("Этот треугольник прямоугольный")
else:
    print("Этот треугольник разносторонный")

