#1
class Spell:
    def __init__(self, spell_name: str, spell_lvl: int, spell_type: str, spell_description: str):
        self.__spell_name = spell_name
        self.__spell_lvl = spell_lvl
        self.__spell_type = spell_type
        self.__spell_description = spell_description

    def get_spell_name(self):
        return self.__spell_name

    def get_spell_lvl(self):
        return self.__spell_lvl

    def get_spell_type(self):
        return self.__spell_type

    def get_spell_description(self):
        return self.__spell_description


    def set_spell_name(self, set_name: str):
        self.__spell_name = set_name

    def set_spell_lvl(self, set_lvl: int):
        self.__spell_lvl = set_lvl

    def set_spell_type(self, set_type: str):
        self.__spell_type = set_type

    def self_spell_description(self, set_description: str):
        self.__spell_description = set_description


    def __str__(self):
        return ("Название заклинания ->", self.__spell_name,
                "Уровень заклинания ->", self.__spell_lvl,
                "Тип заклинания ->", self.__spell_type,
                "Описания заклинания ->", self.__spell_description)



class Wizard:
    def __init__(self, wiz_name: str, wiz_faculty: str, magic_power_lvl: int, spells_list: list[Spell], wiz_status: str):
        self.__wiz_name = wiz_name
        self.__wiz_faculty = wiz_faculty
        self.__magic_power_lvl = magic_power_lvl
        self.__spells_list = spells_list
        self.__wiz_status = wiz_status

    def get_name(self):
        return self.__wiz_name

    def get_house(self):
        return self.__wiz_faculty

    def get_magic_lvl(self):
        return self.__magic_power_lvl

    def get_spells(self):
        return f"{self.__spells_list}" if self.__spells_list != [] else "Список пуст."

    def get_status(self):
        return self.__wiz_status


    def set_house(self, house: str):
        self.__wiz_faculty = house

    def set_magic_lvl(self, set_lvl: int):
        if set_lvl >= 0:
            self.__magic_power_lvl = set_lvl

    def set_status(self, set_status: str):
        self.__wiz_status = set_status

    def add_spell(self, spell: Spell):
        self.__spells_list.append(spell)

    def remove_spell(self, spell: Spell):
        self.__spells_list.remove(spell)

    def increase_magic_lvl(self, amount: int):
        if self.__magic_power_lvl >= 0:
            self.__magic_power_lvl += amount

    def __str__(self):
        return f"Имя волшебника -> {self.__wiz_name}\nФакультет волшебника -> {self.__wiz_faculty}\nУровень магической силы -> {self.__magic_power_lvl}\nЗаклинания волшебника ->", f"{self.__spells_list}" if self.__spells_list != [] else "Нет", f"\nТекущий статус волшебника -> {self.__wiz_status}"


spell_1 = Spell("Дифунксий", 4, "Лесной", "Лечит сущность на 10 HP.")

timbersaw = Wizard("Тимбер", "Факультет вырубки леса", 6, [], "Выпущен")



#2
class Project:
    def __init__(self, name_project: str, date_year_project: int, perf_project: bool):
        self.__name_project = name_project
        self.__date_year_project = date_year_project
        self.__perf_project = perf_project


class Employee:
    def __init__(self, name_emp: str, post_emp: str, division_emp: str, salary_emp: int, experience_emp: int, projects_emp: list):
        self.__name_emp = name_emp
        self.__post_emp = post_emp
        self.__division_emp = division_emp
        self.__salary_emp = salary_emp
        self.__experience_emp = experience_emp
        self.__projects_emp = projects_emp

    def add_project(self, project):
        self.__projects_emp.append(Project)
        print("Проект добавлен!")

    def set_name(self, name: str):
        self.__name_emp = name

    def set_post(self, post: str):
        self.__post_emp = post

    def set_division(self, division: str):
        self.__division_emp = division

    def set_salary(self, salary: int):
        self.__salary_emp = salary

    def set_experience(self, experience: int):
        self.__experience_emp = experience

    def set_projects(self, projects: list[Project]):
        self.__projects_emp = projects

    def get_name(self):
        print(f"{self.__name_emp}")

    def get_post(self):
        print(f"{self.__post_emp}")

    def get_division(self):
        print(f"{self.__division_emp}")

    def get_salary(self):
        print(f"{self.__salary_emp}")

    def get_experience(self):
        print(f"{self.__experience_emp}")

    def get_projects(self):
        if self.__projects_emp != []:
            print(f"Список проектов -> {self.__projects_emp}")
        else:
            print("Список пуст!")

    def __str__(self):
        return f"Имя: {self.__name_emp}\nДолжность: {self.__post_emp}\nОтдел: {self.__division_emp}\nЗарплата: {self.__salary_emp}\nСтаж: {self.__experience_emp}\nСписок проектов:{self.__projects_emp}"


project_1 = Project("Игрулька", 2025, False)

grisha = Employee("Гриша", "девопс", "разработка текстов", 270000, 2, [])

grisha.add_project(project_1)
#grisha.get_projects_list() # ???