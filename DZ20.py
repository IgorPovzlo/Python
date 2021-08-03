print("Домашнее задание №20. Задача на словари 1")
words = input("Введите строку").split()

dictionary = {}

for word in words:
    if word not in dictionary:
        dictionary[word]= 1
    else:
        dictionary[word]+= 1

print (dictionary)
