print("Домашнее задание №16. Ромб 1")
rows = int(input("Введите высоту фигуры"))
if rows % 2 == 0:
    rows += 1
cols = rows

for i in range(rows):
    for j in range(cols):
        if rows/2 >= i :
            if j == (rows//2-i) or j == (rows//2+i) or i == rows//2 :
                print("+ ", end="")
            else:
                print("  ", end="")

        if rows / 2 < i:
            if j == i-rows//2 or j == (cols -i-1)+cols//2:
                print("+ ", end="")
            else:
                print("  ", end="")
    print()