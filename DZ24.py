# Домашнее задание №24. Функция is_year_leap
def is_year_leap(year):
    if year % 4 != 0 :
        return False
    elif year % 100 == 0 :
        if year % 400 == 0 :
            return True
        else :
            return False
    else :
        return True

print(is_year_leap(int(input("Введите год:"))))