print("Домашнее задание №5. Шахматный конь")
x1 = int(input("Введите начальную координату x" ))
y1 = int(input("Введите начальную координату y" ))
x2 = int(input("Введите кординату перемещения коня по x" ))
y2 = int(input("Введите кординату перемещения коня по x" ))
dx = abs(x1 - x2)
dy = abs(y1 - y2)
if x1 <= 8 and y1 <=8 and x2 <=8 and y2 <=8:
    if dx == 1 and dy == 2 or dx == 2 and dy == 1:
        print("Конь может пойти на данную клетку")
    else:
        print("Конь не может пойти на данную клетку")
else :
    print("Введеные координаты не являются координатами шахматной доски " )