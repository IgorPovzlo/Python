# Домашнее задание №30. Конвертер чисел
def converter(number, number_system):
    a = [0, 1 , 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    b = ''

    while number > 0:
        b = str(a[number % number_system]) + b
        number = number // number_system

    print(b)

x = converter(int(input('Введите число в десятичной системе счисления:')),
               int(input('Введите систему счисления в которою необходимо перевести(2-36) :')))

