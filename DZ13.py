print("Домашнее задание №13.Замена символов в строке:")
str1 = input("Введите строку:")
a = str1[:str1.find('h') + 1]
b = str1[str1.find('h') + 1:str1.rfind('h')]
c = str1[str1.rfind('h'):]
str1 = a + b.replace('h', 'H') + c
print(str1)