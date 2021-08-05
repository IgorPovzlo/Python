# Домашнее задание №25. Функция season
def season(month):
    if 0 < month <= 12 :
        if month == 12 or 1 <= month <= 2:
            return "Зима"
        if 3 <= month <= 5:
            return "Весна"
        if 6 <= month <= 8:
            return "Лето"
        if 9 <= month <= 11:
            return "Осень"
    else:
        return "Не корректные данные"

print(season(int(input("Введите номер месяца:"))))