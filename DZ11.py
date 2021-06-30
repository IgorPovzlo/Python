print("Домашнее задание №11. Поиск символа в строке")
str1 = input("Введите строку:")
f = input("Введите символ который нужно найти:")
s = 0
while str1.find(f, s) > -1:
    print(str1.find(f,s))
    s = str1.find(f,s) + 1

