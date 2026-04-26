class Rectangle:
    def __init__(self, width: int | float, height: int | float) -> None:
        self.width = width
        self.height = height

    def area(self) -> int | float:
        return self.width * self.height

    def perimeter(self) -> int | float:
        return 2 * (self.width + self.height)


rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)
rect3 = Rectangle(8, 4)

print("Прямоугольник 1:")
print("Площадь:", rect1.area())
print("Периметр:", rect1.perimeter())

print("Прямоугольник 2:")
print("Площадь:", rect2.area())
print("Периметр:", rect2.perimeter())

print("Прямоугольник 3:")
print("Площадь:", rect3.area())
print("Периметр:", rect3.perimeter())


class Math:
    def __init__(self) -> None:
        self.a = 0
        self.b = 0

    def addition(self, a: int | float, b: int | float) -> None:
        self.a = a
        self.b = b
        print(self.a + self.b)

    def multiplication(self, a: int | float, b: int | float) -> None:
        self.a = a
        self.b = b
        print(self.a * self.b)

    def division(self, a: int | float, b: int | float) -> None:
        self.a = a
        self.b = b
        if self.b != 0:
            print(self.a / self.b)
        else:
            print("На ноль делить нельзя")

    def subtraction(self, a: int | float, b: int | float) -> None:
        self.a = a
        self.b = b
        print(self.a - self.b)


calc = Math()
calc.addition(10, 5)
calc.multiplication(10, 5)
calc.division(10, 5)
calc.subtraction(10, 5)


class Button:
    def __init__(self, text: str, button_type: str = "Кнопка", locator: str = "") -> None:
        self.text = text
        self.button_type = button_type
        self.locator = locator

    def click(self) -> str:
        return f"Клик по кнопке {self.text}"


text_box = Button("Text Box")
check_box = Button("Check Box")
radio_button = Button("Radio Button")
web_tables = Button("Web Tables")
buttons = Button("Buttons")
links = Button("Links")
broken_links_images = Button("Broken Links - Images")
upload_download = Button("Upload and Download")
dynamic_properties = Button("Dynamic Properties")

all_buttons = [
    text_box,
    check_box,
    radio_button,
    web_tables,
    buttons,
    links,
    broken_links_images,
    upload_download,
    dynamic_properties
]

for button in all_buttons:
    print(button.text)

for button in all_buttons:
    print(button.click())


