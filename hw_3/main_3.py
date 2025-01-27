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
        return f"Название заклинания -> {self.__spell_name}\nУровень заклинания -> {self.__spell_lvl}\nТип заклинания -> {self.__spell_type}\nОписания заклинания -> {self.__spell_description}"



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

    def add_salary(self, salary: int):
        self.__salary_emp += salary
        print("Текущая зарплата ->", self.__salary_emp)

    def delete_project(self, project):
        if project not in self.__projects_emp:
            print("Проект не был найден.")
        else:
            self.__projects_emp.remove(project)
            print("Проект удалён!")


project_1 = Project("Игрулька", 2025, False)

grisha = Employee("Гриша", "девопс", "разработка текстов", 270000, 2, [])

#grisha.add_project(project_1)
#grisha.get_projects_list() # ???


#3
class Task:
    def __init__(self, name_task: str, time_minute_task: int, status_task: bool = False):
        self.__name_task = name_task
        self.__time_minute_task = time_minute_task
        self.__status_task = status_task


class Robot:
    def __init__(self, factory_number_robot: int, model_robot: str, task_robot: str, batary_lvl_robot: int, status_robot: str):
        self.__factory_number_robot = factory_number_robot
        self.__model_robot = model_robot
        self.__task_robot = task_robot
        self.__batary_lvl_robot = batary_lvl_robot
        self.__status_robot = status_robot

    def new_task(self, task: str):
        if task.status_task and task != self.__task_robot: # ???
            self.__task_robot = task
            print("Новая задача поставлена!")
        else:
            print("Задача не изменена.")

    def change_batary_lvl(self, lvl: int):
        if self.__batary_lvl_robot != lvl and lvl > -1:
            self.__batary_lvl_robot = lvl
            print("Уровень батареи обновлён!")
        else:
            print("Уровень батареи не изменён.")

    def change_status(self, status: bool):
        if status != self.__status_robot:
            self.__status_robot = status
            if self.__status_robot:
                print("Робот перешёл в активное состояние.")
            else:
                print("Робот ушёл на перерыв.")
        else:
            print("Статус не изменён.")

    def set_factory_number(self, factory_number: int):
        self.__factory_number_robot = factory_number
        print("Успешно!")


    def set_model(self, model: str):
        self.__model_robot = model
        print("Успешно!")

    def set_task(self, task: str):
        self.__task_robot = task
        print("Успешно!")

    def set_batary_lvl(self, batary_lvl: int):
        self.__batary_lvl_robot = batary_lvl
        print("Успешно!")

    def get_factory_number(self):
        print(self.__factory_number_robot)

    def get_model(self):
        print(self.__model_robot)

    def get_task(self):
        print(self.__task_robot)

    def get_batary(self):
        print(self.__batary_lvl_robot)

    def get_status(self):
        print(self.__status_robot)

    def __str__(self):
        return f"Серийный номер: {self.__factory_number_robot}\nМодель: {self.__model_robot}\nЗадача: {self.__task_robot}\nУровень заряда ботареи: {self.__batary_lvl_robot}\nСтатус: {self.__status_robot}"

task_1 = Task("Сортировка", 15)

robot_connor = Robot(11244109, "Базовый андроид", "Сортировка", 87, "Перерыв")


#3
class Achievement:
    def __init__(self, sport: str, year_got: int, quality: str):
        self.__sport = sport
        self.__year_got = year_got
        self.__quality = quality


class Athlete:
    def __init__(self, name_athlete: str, age_athlete: int, sport_athlete: str, achievements_athlete: list, pension_athlete: bool):
        self.__name_athlete = name_athlete
        self.__age_athlete = age_athlete
        self.__sport_athlete = sport_athlete
        self.__achievements_athlete = achievements_athlete
        self.__pension_athlete = pension_athlete

    def add_achievement(self, achievement):
        if achievement not in self.__achievements_athlete:
            self.__achievements_athlete.append(achievement)
            print("Успешно!")
        else:
            print("Список не обновлён.")

    def delete_achievement(self, achievement):
        if achievement not in self.__achievements_athlete:
            self.__achievements_athlete.remove(achievement)
            print("Успешно!")
        else:
            print("Список не обновлён.")

    def set_name(self, name: str):
        self.__name_athlete = name

    def set_age(self, age: int):
        self.__age_athlete = age

    def set_sport(self, sport: str):
        self.__sport_athlete = sport

    def set_status(self, pension: bool):
        self.__pension_athlete = pension

    def get_name(self):
        print(self.__name_athlete)

    def get_age(self):
        print(self.__age_athlete)

    def get_sport(self):
        print(self.__sport_athlete)

    def get_achievements(self):
        if self.__achievements_athlete != []:
            print(self.__achievements_athlete)
        else:
            print("Достижений нет!")

    def get_pension(self):
        if self.__pension_athlete:
            print("Да")
        else:
            print("Нет")

    def __str__(self):
        return f"Имя: {self.__name_athlete}\nВозраст: {self.__age_athlete}\nСпорт: {self.__sport_athlete}\nСписок достижений: {"Нет" if self.__achievements_athlete == [] else self.__achievements_athlete}\nСтатус пенсии: {"Да" if self.__pension_athlete else "Нет"}"


achievement_1 = Achievement("Лыжный спорт", 2009, "Золото")

vasia = Athlete("Вася", 36, "Лыжный спорт", [], True)