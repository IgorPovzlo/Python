from random import randint

M = int(input("Ведите количество строк:"))
N = int(input("Введите количество колонок:"))

lst = [[randint(10, 99) for _ in range(N)] for _ in range(M)]
tmp_lst = [0]*N
tmp = '{:5}'

for i in range(M):
    S = 0
    for j in range(N):
        print(tmp.format(lst[i][j]), end=' ')
        S += lst[i][j]
        tmp_lst[j] += lst[i][j]
    print('\t\t', S)
print()

for value in tmp_lst:
    print(tmp.format(value), end=' ')