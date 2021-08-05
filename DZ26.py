# Домашнее задание №25. Функция arithmetic

def arithmetic():  #(a, b, operation):  #Нужно будет указывать атрибуты во время вызова функции
    a = int(input("Введите первое число:"))
    b = int(input("Введите второе число:"))
    operation = input("Введите операцию:")

    if operation == "+":
        return a+b
    if operation == "-":
        return a-b
    if operation == "*":
        return a*b
    if operation == "/":
        return a/b
    else:
        return "Неизвестная операция"

print(arithmetic())

