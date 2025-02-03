class Student:
    name: str
    second_name: str
    age: int
    middle_point: int

    def __init__(self, name: str, second_name: str, age: int, middle_point: int):
        self.__name = name
        self.__second_name = second_name
        self.__age = age
        self.__middle_point = middle_point

        if not isinstance(name, str):
            raise ValueError("NameTypeError")
        if not isinstance(second_name, str):
            raise ValueError("SecondNameTypeError")
        if age > -1 and not isinstance(age, int):
            raise ValueError("AgeTypeError")
        if not isinstance(middle_point, str):
            raise ValueError("MiddlePointTypeError")

    def get_name(self) -> str:
        return self.__name
    def get_second_name(self) -> str:
        return self.__second_name
    def get_age(self) -> int:
        return self.__age
    def get_middle_point(self) -> int:
        return self.__middle_point

    def set_name(self, other: str):
        self.__name = other
    def set_second_name(self, other: str):
        self.__second_name = other
    def set_age(self, age: int):
        self.__age = age
    def set_middle_point(self, other: int):
        self.__middle_point = other

    def __str__(self):
        return f"Имя: {self.__name}\nФамилия: {self.__second_name}\nВозраст: {self.__age}\nСредний балл: {self.__middle_point}"

    def __eq__(self, other: int) -> bool:
        return self.__middle_point == other
    def __lt__(self, other: int) -> bool:
        return self.__middle_point < other
    def __gt__(self, other: int) -> bool:
        return self.__middle_point > other
    def __le__(self, other: int) -> bool:
        return self.__middle_point <= other
    def __ge__(self, other: int) -> bool:
        return self.__middle_point >= other