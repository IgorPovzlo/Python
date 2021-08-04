# print("Домашнее задание №22. Задача на словари 2")
words = input("Введите строку").split()

dictionary = {}

for word in words:
    if word not in dictionary:
        dictionary[word] = 1
    else:
        dictionary[word] += 1
max_count = max(dictionary.values())
most_frequent = [i for i, j in dictionary.items() if j == max_count]
print(most_frequent[-1])
