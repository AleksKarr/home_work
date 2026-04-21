def task_1() -> None:
    age: int = 25
    price: float = 19.99
    name: str = "Алекс"
    items: list = [1, 2, 3]
    is_active: bool = True

    print(type(age))
    print(type(price))
    print(type(name))
    print(type(items))
    print(type(is_active))


task_1()


def task_2() -> None:
    a: list[int] = [1, 2, 3, 5, 8, 13, 21]
    print(a[:3])


task_2()
# Это последовательность Фибоначчи

def task_3(num: int) -> int:
    return num ** 2


print(task_3(5))

print (" all it Ok")

