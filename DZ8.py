print("Домашннее задание №8. Наибольшая целая степень двойки")
N = int(input("Введите число:"))
a = 0
b = 1
while b * 2 <= N:
    b *= 2
    a += 1
print(a , "- Показатель степени")
print(b , "- Степень")