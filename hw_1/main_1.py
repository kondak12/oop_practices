# 1
class Animal:
    def __init__(self, name: str, animal_type: str, age: int, sound = "Мяу!"):
        self.name = name
        self.animal_type = animal_type
        self.age = age
        self.sound = sound

    def play_sound(self):
        return print(self.sound)

    def all_thinks_animal(self):
        return print(f"Имя -> {self.name} \n"
                     f"Вид -> {self.animal_type} \n"
                     f"Возраст -> {self.age}")


cat = Animal("Барсик", "Кот", 3)

cat.all_thinks_animal()
cat.play_sound()



# 2
class Book:
    def __init__(self, book_name: str, book_author: str, book_info: str, book_amount: int):
        self.book_name = book_name
        self.book_author = book_author
        self.book_amount = book_amount
        self.book_info = book_info

    def book_str(self, book_enter: int):
        if book_enter <= self.book_amount and book_enter != 999:
            print("Страница открылась!")

        elif book_enter != 999:
            print("Страницы не существует!")

        elif book_enter == 999:
            print(self.book_info)

    def book_function(self):
        print(f"\nВведите № страницы для её открытия (Макс. {self.book_amount}) / '999' - для информации о книге")
        enter_num = int(input("Введите команду >> "))
        self.book_str(enter_num)


book1 = Book("История обо мне", "Я", "Я написал эту книгу!", 100)

book1.book_function()



# 3
class PassangerPlane:
    def __init__(self, airplane_now: str, made_by: str, airplane_model: str, airplane_sits_amount: int, passangers: int, air_height: int, air_speed: int):
        self.airplane_now = airplane_now
        self.made_by = made_by
        self.airplane_model = airplane_model
        self.airplane_sits_amount = airplane_sits_amount
        self.passangers = passangers
        self.air_height = air_height
        self.air_speed = air_speed

    def airplan_action(self):
        airplane_mode = 1

        while airplane_mode == 1:
            airplane_input = str(input("\nВзлёт / Посадка / Высота / Инфо / Выход >> "))

            if airplane_input.lower() == "взлет" or airplane_input.lower() == "взлёт":
                self.air_height = 8
                self.airplane_now = "В полёте"
                print("Самолёт взлетел!")

            if airplane_input.lower() == "посадка":
                self.air_height = 0
                self.airplane_now = "На земле"
                print("Самолёт приземлился")

            if airplane_input.lower() == "высота":
                self.air_height = int(input("Введите новую высоту самолёта >> "))

            if airplane_input.lower() == "инфо":
                print(f"\nСостояние полёта -> {self.airplane_now} \n"
                 f"Произведён -> {self.made_by} \n"
                 f"Модель самолёта -> {self.airplane_model} \n"
                 f"Количество мест -> {self.airplane_sits_amount} \n"
                 f"Количество пассажиров -> {self.passangers} \n"
                 f"Высота полёта -> {self.air_height} \n"
                 f"Скорость полёта -> {self.air_speed}")

            if airplane_input.lower() == "выход":
                airplane_mode = 0


airplane1 = PassangerPlane("На земле", "China", "1231-B", 100, 80, 8, 500)
airplane1.airplan_action()



# 4 - Не успел :(