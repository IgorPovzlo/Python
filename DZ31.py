# Домашнее задание №31. Реверс списка
def reverse(x):
    for i in range(int(len(x)/2)):
        x[i],x[-1-i] = x[-1-i],x[i]
    return x

x = [0,1,2,3,4,5,6,7,8,9]
print(x)
r = reverse(x)
print(r)