from random import randint

def bubble_sort(array, lst1):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                for k in range(M):
                    lst1[k][j], lst1[k][j + 1] = lst1[k][j + 1], lst1[k][j]

    for q in range(M):
        for u in range(M-1):
            for p in range(M):
                if p % 2 == 0:
                    if lst1[u][p] > lst1[u + 1][p]:
                        lst1[u][p], lst1[u + 1][p] = lst1[u + 1][p], lst1[u][p]
                else:
                    if lst1[u][p] < lst1[u + 1][p]:
                        lst1[u][p], lst1[u + 1][p] = lst1[u + 1][p], lst1[u][p]


def print_lst(lst2):
    tmp = '{:4}'
    for i in range(M):
        for j in range(M):
            tmp_lst[j] += lst2[i][j]
            print(tmp.format(lst2[i][j]), end=' ' )

        print()
    print()

    for value in tmp_lst:
        print(tmp.format(value), end=' ')
    print()

M = int(input('Введите размер стороны матрицы:'))
lst = [[randint(1, 50) for _ in range(M)] for _ in range(M)]
tmp_lst = [0] * M

print('До сортировки:')
print_lst(lst)

bubble_sort(tmp_lst, lst)
tmp_lst = [0] * M

print('После сортировки:')
print_lst(lst)
