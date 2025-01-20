import datetime

class Patient:
    def __init__(self, name: str, second_name: str, dad_name: str, age: int, viruses: str):
        self.name = name
        self.second_name = second_name
        self.dad_name = dad_name
        self.age = age
        self.viruses = viruses
        self.date = datetime.datetime.now()

    def __str__(self):
        return ("Имя пациента - " + f"{self.name}", f"{self.second_name}", f"{self.dad_name}",
                "\nВозраст - " + f"{self.age}",
                "\nЗаболевания - " + f"{self.viruses}")

    def hospital_date(self):
        return "Дата записи пациента - " + f"{self.date}"



class TouristSpot:
    def __init__(self, spot_name: str, spots_country: str, spot_type: str):
        self.spot_name = spot_name
        self.spots_country = spots_country
        self.spot_type = spot_type

    def go_to_spot(self, spots_visitor):
        return f"{spots_visitor}", "посетил" + f"{self.spot_name}"

    def __str__(self):
        return (("Достопримечательность - " + f"{self.spot_name}",
                "\nРасположение достопримечательности - " + f"{self.spots_country}"),
                "\nТип достопримечательности - " + f"{self.spot_type}")



class ModelWindow:
    def __init__(self, window_title: str, window_left_t_coordinates: list[int, int], window_color: str, horizontal_size: int, vertical_size: int, window_state_visibility: bool, window_frame_state: bool):
        self.window_title = window_title
        self.window_left_t_coordinates = window_left_t_coordinates
        self.window_color = window_color
        self.horizontal_size = horizontal_size
        self.vertical_size = vertical_size
        self.window_state_visibility = window_state_visibility
        self.window_frame_state = window_frame_state

    @staticmethod
    def window_size_controller(place_mode: int, new_place: int):
        if place_mode == 1:
            if 0 <= new_place <= 1080:
                return True
            else:
                return False
        if place_mode == 2:
            if 0 <= new_place <= 1960:
                return True
            else:
                return False

    def window_replace_horizontal(self, new_horizontal_place: int):
        size_state = ModelWindow.window_size_controller(1, new_horizontal_place)
        if size_state:
            return new_horizontal_place
        else:
            return "Ошибка!"

    def window_replace_vertical(self, new_vertical_place: int):
        size_state = ModelWindow.window_size_controller(2, new_vertical_place)
        if size_state:
            return new_vertical_place
        else:
            return "Ошибка!"

    def window_size_horizontal(self, new_horizontal_size: int):
        size_state = ModelWindow.window_size_controller(1, new_horizontal_size)
        if size_state:
            return new_horizontal_size
        else:
            print("Ошибка!")

    def window_size_vertical(self, new_verticacl_size: int):
        size_state = ModelWindow.window_size_controller(2, new_verticacl_size)
        if size_state:
            return new_verticacl_size
        else:
            print("Ошибка!")

    def rechange_window_color(self, new_color: str):
        if new_color.lower() != self.window_color.lower():
            return new_color
        else:
            print("Цвет не был изменён.")

    def rechange_window_visibility(self):
        if self.window_state_visibility == True:
            self.window_state_visibility = False
        elif self.window_state_visibility == False:
            self.window_state_visibility = True

    def window_visibility_status(self):
        if self.window_state_visibility == True:
            return "Окно видно."
        else:
            return "Окно не видно."

    def __str__(self):
        return ("Заголовок окна - " + f"{self.window_title}",
                "\nРасположение левого угла окна - " + f"{self.window_left_t_coordinates[0], "/", self.window_left_t_coordinates[1]}",
                "\nЦвет окна - " + f"{self.window_color}",
                "\nРазмер окна по горизонтали - " + f"{self.horizontal_size}",
                "\nРазмер окна по вертикали - " + f"{self.vertical_size}",
                "\nСтатус видимости окна - " + f"{self.window_state_visibility}",
                "\nРамка окна - " + f"{self.horizontal_size, "/", self.vertical_size}")



class ArraysUtils:
    def nums_sum(self, other: list):
        summ = 0
        for i in other:
            summ += i
        return summ

    def nums_mul(self, other: list):
        mul = 1
        for i in other:
            mul *= i
        return mul

    def nums_inverse(self, other: list):
        inv_list = []
        for i in range(len(other) + 1):
            inv_list.append(other[-i])
        return inv_list

    def find_max(self, other: list):
        max_element = 0
        for i in other:
            if i >= max_element:
                max_element = i
        return max_element

    def find_min(self, other: list):
        min_element = other[0]
        for i in other:
            if i <= min_element:
                min_element = i
        return min_element