# Домашнее задание №23. Функция square
def square(side):
    P = 4 * side
    S = side * side
    d = (2*S) ** 0.5

    k = (P, S, d)
    return k

print(square(int(input("Введите сторону квадрата:"))))