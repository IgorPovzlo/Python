print("Домашнее задание №22. Инвертирование словаря")

d = {
   'apple': ['malum', 'pomum', 'popula'],
   'fruit': ['baca', 'bacca', 'popum'],
   'punishment': ['malum', 'multa']
}
d1={}
for a,b in d.items():
  for item in b:
    if item in d1:
      d1[item].append(a)
    else:
      d1[item] = [a]

print(d)
print(d1)

