class Car:
    def __init__(self, color: str = "", car_type: str = "", year: int = 0) -> None:
        self.color = color
        self.type = car_type
        self.year = year

    def start(self) -> None:
        print("Автомобиль заведен")

    def stop(self) -> None:
        print("Автомобиль заглушен")

    def set_year(self, year: int) -> None:
        self.year = year

    def set_type(self, car_type: str) -> None:
        self.type = car_type

    def set_color(self, color: str) -> None:
        self.color = color


car = Car()
car.start()
car.set_year(2020)
car.set_type("Седан")
car.set_color("Черный")
car.stop()

print(car.year)
print(car.type)
print(car.color)