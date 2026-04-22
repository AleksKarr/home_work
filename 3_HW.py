# Задача 2


def max_number(a: int | float, b: int | float) -> None:
    print(max(a, b))

max_number(7, 12)

def difference_135(a: int | float, b: int | float) -> None:
    if abs(a - b) == 135:
        print("yes")
    else:
        print("No")

difference_135(200, 65)


def season_by_month(month: int) -> None:
    if month in (12, 1, 2):
        print("зима")
    elif month in (3, 4, 5):
        print("весна")
    elif month in (6, 7, 8):
        print("лето")
    elif month in (9, 10, 11):
        print("осень")
    else:
        print("Некорректный номер месяца")

season_by_month(4)


def all_more_than_ten(a: int | float, b: int | float, c: int | float) -> None:
    if a > 10 and b > 10 and c > 10:
        print("yes")
    else:
        print("no")

all_more_than_ten(11, 15, 20)


def count_positive_numbers(numbers: list[int | float]) -> None:
    count = 0
    for num in numbers:
        if num > 0:
            count += 1
    print(count)


count_positive_numbers([1, -2, 3, 0, 5])


def count_days(years: int, months: int) -> None:
    total_months = years * 12 + months
    days = total_months * 29
    print(days)


count_days(2, 3)

