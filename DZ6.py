print("Домашнее задание №6.Высокосный год")
x = int(input("Введите год:"))
if x % 4 != 0 :
    print(x , "- это не высокосный год" )
elif x % 100 == 0 :
    if x % 400 == 0 :
        print(x , "- это высокосный год" )
    else :
        print(x , "- это не высокосный год" )
else :
    print(x , "- это высокосный год" )
