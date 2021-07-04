print("Домашнее задание №15. Треугольник 2")
rows = int(input("Введите высоту треугольника"))
if rows % 2 == 0:
    rows += 1
cols = rows*2-1
for i in range(rows):
    for j in range(cols):
        if j == (rows-1)+i or j == (rows-1)-i or i == rows - 1 or  j+i >= rows-1 and j-i<= rows -1 :
            print("+ ", end="")
        else:
            print("  ", end="")
    print()
