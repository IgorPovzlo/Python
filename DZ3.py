print("Домашнее задание №3.Математические классы")
a = int(input("Введите количество учеников в первом классе:"))
b = int(input("Введите количество учеников во втором классе:"))
c = int(input("Введите количество учеников в третьем классе:"))
x = (a // 2)+(a % 2)+(b // 2)+(b % 2)+(c // 2)+(c % 2)
print("Количество парт которые нужно закупить ", x)