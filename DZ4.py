print("Домашнее задание №4.Перевернуть число")
a = int(input("Введите целое трёхзначное число:"))
b = a%10
a = a//10
c = a%10
a = a//10
d = a%10
#x = b, c, d,
x = int(str(b)+str(c)+str(d))
print("Обратное  число:", x)