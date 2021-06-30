print("Домашнее задание №11. Поиск символа в строке")
s = input("Введите строку:")
f = input("Введите символ который нужно найти:")
sub = 0
while s.find(f, sub) > -1 :
    sub == s.find(f, sub)+1
    print(s.find(f))

