print("Домашнее задание №22. Задача на словари 2")
words = input("Введите строку").split()

dictionary = {}

for word in words:
    if word not in dictionary:
        dictionary[word]= 1
    else:
        dictionary[word]+= 1
d= max(dictionary.values())
print(d)
print (dictionary)
