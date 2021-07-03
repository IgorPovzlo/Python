print("Домашнее задание №14. Треугольник 1")
rows = int(input("Введите высоту треугольника"))
cols = rows*2-1
for i in range(rows):
    for j in range(cols):
        if j == (rows-1)+i or j == (rows-1)-i or i == rows - 1 :
            print("+ ", end="")
        else:
            print("  ", end="")
    print()
