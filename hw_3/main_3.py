#1
class Spell:
    name: str
    level: int
    type_spell: str
    description: str

    def __init__(self, name: str, level: int, spell_type: str, description: str):
        self.__name = name
        self.__level = level
        self.__type_spell = spell_type
        self.__description = description

        if not isinstance(name, str):
            raise ValueError("NameTypeError")
        if not isinstance(level, int):
            raise ValueError("LevelTypeError")
        if not level > -1:
            raise ValueError("TypeError")
        if not isinstance(spell_type, str):
            raise ValueError("SpellTypeTypeError")
        if not isinstance(description, str):
            raise ValueError("DescriptionTypeError")

    def get_spell_name(self):
        return self.__name

    def get_spell_lvl(self):
        return self.__level

    def get_spell_type(self):
        return self.__type_spell

    def get_spell_description(self):
        return self.__description


    def set_spell_name(self, other: str):
        self.__name = other

    def set_spell_lvl(self, other: int):
        self.__level = other

    def set_spell_type(self, other: str):
        self.__type_spell = other

    def self_spell_description(self, other: str):
        self.__description = other


    def __str__(self):
        return f"Название заклинания -> {self.__name}\nУровень заклинания -> {self.__level}\nТип заклинания -> {self.__type_spell}\nОписания заклинания -> {self.__description}"



class Wizard:
    name: str
    faculty: str
    magic_power_level: int
    spells_list: list[Spell]
    status = {'В Хогвартсе': 1, 'Выпустился': 2}

    def __init__(self, name: str, faculty: str, magic_power_level: int, spells_list: list[Spell], status: int):
        self.__name = name
        self.__faculty = faculty
        self.__magic_power_level = magic_power_level
        self.__spells_list = spells_list
        self.__status = status

        if not isinstance(name, str):
            raise ValueError("NameTypeError")
        if not isinstance(faculty, str):
            raise ValueError("FacultyTypeError")
        if not isinstance(magic_power_level, int):
            raise ValueError("MagicPowerLevelTypeError")
        if not spells_list is list[Spell]:
            raise ValueError("SpellsListTypeError")
        if not isinstance(status, int):
            raise ValueError("StatusTypeError")

    def get_name(self):
        return self.__name

    def get_house(self):
        return self.__faculty

    def get_magic_lvl(self):
        return self.__magic_power_level

    def get_spells(self):
        return f"{self.__spells_list}" if self.__spells_list != [] else "Список пуст."

    def get_status(self):
        return self.__status


    def set_house(self, house: str):
        self.__faculty = house

    def set_magic_level(self, set_level: int):
        if set_level >= 0:
            self.__magic_power_level = set_level

    def set_status(self, set_status: str):
        self.__status = set_status

    def add_spell(self, spell: Spell):
        self.__spells_list.append(spell)

    def remove_spell(self, spell: Spell):
        self.__spells_list.remove(spell)

    def increase_magic_lvl(self, amount: int):
        if self.__magic_power_level >= 0:
            self.__magic_power_level += amount

    def __str__(self):
        return f"Имя волшебника -> {self.__name}\nФакультет волшебника -> {self.__faculty}\nУровень магической силы -> {self.__magic_power_level}\nЗаклинания волшебника ->", f"{self.__spells_list}" if self.__spells_list != [] else "Нет", f"\nТекущий статус волшебника -> {self.__status}"


spell_1 = Spell("Дифунксий", 4, "Лесной", "Лечит сущность на 10 HP.")

timbersaw = Wizard("Тимбер", "Факультет вырубки леса", 6, [], "Выпущен")



#2
class Project:
    name: str
    date_year: int
    perf: bool

    def __init__(self, name: str, date_year: int, perf: bool):
        self.__name = name
        self.__date_year = date_year
        self.__perf = perf

        if not isinstance(name, str):
            raise ValueError("NameTypeError")
        if not isinstance(date_year, int):
            raise ValueError("DateTypeError")
        if not isinstance(perf, bool):
            raise ValueError("PerfTypeError")


class Employee:
    name: str
    post: str
    division: str
    salary: int
    experience: int
    projects = None

    def __init__(self, name: str, post: str, division: str, salary: int, experience: int, projects = None):
        self.__name = name
        self.__post = post
        self.__division = division
        self.__salary = salary
        self.__experience = experience
        self.__projects = projects

        if not isinstance(name, str):
            raise ValueError("NameTypeError")
        if not isinstance(post, str):
            raise ValueError("PostTypeError")
        if not isinstance(division, str):
            raise ValueError("DivisionTypeError")
        if not isinstance(salary, int):
            raise ValueError("SalaryTypeError")
        if not isinstance(experience, int):
            raise ValueError("ExpTypeError")
        if not isinstance(projects, None or list):
            raise ValueError("TypeError")

    def add_project(self, project: Project):
        self.__projects.append(project)
        print("Проект добавлен!")

    def set_name(self, name: str):
        self.__name = name

    def set_post(self, post: str):
        self.__post = post

    def set_division(self, division: str):
        self.__division = division

    def set_salary(self, salary: int):
        self.__salary = salary

    def set_experience(self, experience: int):
        self.__experience = experience

    def set_projects(self, projects: list[Project]):
        self.__projects = projects

    def get_name(self):
        return f"{self.__name}"

    def get_post(self):
        return f"{self.__post}"

    def get_division(self):
        return f"{self.__division}"

    def get_salary(self):
        return f"{self.__salary}"

    def get_experience(self):
        return f"{self.__experience}"

    def get_projects(self):
        if len(self.__projects) != 0:
            return f"Список проектов -> {self.__projects}"
        else:
            return "Список пуст!"

    def __str__(self):
        return f"Имя: {self.__name}\nДолжность: {self.__post}\nОтдел: {self.__division}\nЗарплата: {self.__salary}\nСтаж: {self.__experience}\nСписок проектов:{self.__projects}"

    def add_salary(self, salary: int):
        self.__salary += salary

    def delete_project(self, project):
        if project not in self.__projects:
            return "Проект не был найден."
        else:
            self.__projects.remove(project)
            return "Проект удалён!"


project_1 = Project("Игрулька", 2025, False)

grisha = Employee("Гриша", "девопс", "разработка текстов", 270000, 2)

grisha.add_project(project_1)
grisha.get_projects()


#3
class Task:
    name: str
    time_minute: int
    status: bool

    def __init__(self, name: str, time_minute: int, status: bool = False):
        self.__name = name
        self.__time_minute = time_minute
        self.__status = status

        if not isinstance(name, str):
            raise ValueError("NameTypeError")
        if not isinstance(time_minute, int):
            raise ValueError("TimeTypeError")
        if not isinstance(status, bool):
            raise ValueError("StatusTypeError")

    def get_status(self):
        return self.__status


class Robot:
    def __init__(self, factory_number: int, model: str, task: str, batary_charge: int, status: str):
        self.__factory_number = factory_number
        self.__model = model
        self.__task = task
        self.__batary_charge = batary_charge
        self.__status = status

        if not isinstance(factory_number, int):
            raise ValueError("FactoryTypeError")
        if not isinstance(model, str):
            raise ValueError("ModelTypeError")
        if not isinstance(task, str):
            raise ValueError("TaskTypeError")
        if not isinstance(batary_charge, int):
            raise ValueError("BataryTypeError")
        if not isinstance(status, str):
            raise ValueError("StatusTypeError")

    def new_task(self, task: Task):
        task_get_status = task.get_status()
        if task_get_status and task != self.__task:
            self.__task = task
            print("Новая задача поставлена!")
        else:
            print("Задача не изменена.")

    def change_batary_lvl(self, lvl: int):
        if self.__batary_charge != lvl and lvl > -1:
            self.__batary_charge = lvl
            print("Уровень батареи обновлён!")
        else:
            print("Уровень батареи не изменён.")

    def change_status(self, status: bool):
        if status != self.__status:
            self.__status = status
            if self.__status:
                print("Робот перешёл в активное состояние.")
            else:
                print("Робот ушёл на перерыв.")
        else:
            print("Статус не изменён.")

    def set_factory_number(self, factory_number: int):
        self.__factory_number = factory_number

    def set_model(self, model: str):
        self.__model = model

    def set_task(self, task: str):
        self.__task = task

    def set_batary_charge(self, charge: int):
        self.__batary_charge = charge


    def get_factory_number(self):
        return self.__factory_number

    def get_model(self):
        return self.__model

    def get_task(self):
        return self.__task

    def get_batary(self):
        return self.__batary_charge

    def get_status(self):
        return self.__status

    def __str__(self):
        return f"Серийный номер: {self.__factory_number}\nМодель: {self.__model}\nЗадача: {self.__task}\nУровень заряда ботареи: {self.__batary_charge}\nСтатус: {self.__status}"

task_1 = Task("Сортировка", 15)

robot_connor = Robot(11244109, "Базовый андроид", "Сортировка", 87, "Перерыв")


#3
class Achievement:
    sport: str
    year_got: int
    quality: str

    def __init__(self, sport: str, year_got: int, quality: str):
        self.__sport = sport
        self.__year_got = year_got
        self.__quality = quality

        if not isinstance(sport, str):
            raise ValueError("SportTypeError")
        if not isinstance(year_got, int):
            raise ValueError("YearTypeError")
        if not isinstance(quality, str):
            raise ValueError("QualityTypeError")


class Athlete:
    name: str
    age: int
    sport: str
    achievement: list
    pension: bool

    def __init__(self, name: str, age: int, sport: str, achievements: list, pension: bool):
        self.__name = name
        self.__age = age
        self.__sport = sport
        self.__achievements = achievements
        self.__pension = pension

        if not isinstance(name, str):
            raise ValueError("NameTypeError")
        if not isinstance(age, int):
            raise ValueError("AgeTypeError")
        if not isinstance(sport, str):
            raise ValueError("SportTypeError")
        if not isinstance(achievements, list):
            raise ValueError("AchievementsTypeError")
        if not isinstance(pension, bool):
            raise ValueError("PensionTypeError")

    def add_achievement(self, achievement):
        if achievement not in self.__achievements:
            self.__achievements.append(achievement)
            print("Успешно!")
        else:
            print("Список не обновлён.")

    def delete_achievement(self, achievement):
        if achievement not in self.__achievements:
            self.__achievements.remove(achievement)
            print("Успешно!")
        else:
            print("Список не обновлён.")

    def set_name(self, name: str):
        self.__name = name

    def set_age(self, age: int):
        self.__age = age

    def set_sport(self, sport: str):
        self.__sport = sport

    def set_status(self, pension: bool):
        self.__pension = pension

    def get_name(self):
        print(self.__name)

    def get_age(self):
        print(self.__age)

    def get_sport(self):
        print(self.__sport)

    def get_achievements(self):
        if len(self.__achievements) != 0:
            return self.__achievements
        else:
            return "Достижений нет!"

    def get_pension(self):
        if self.__pension:
            return "Да"
        else:
            return "Нет"

    def __str__(self):
        return f"Имя: {self.__name}\nВозраст: {self.__age}\nСпорт: {self.__sport}\nСписок достижений: {"Нет" if self.__achievements == [] else self.__achievements}\nСтатус пенсии: {"Да" if self.__pension else "Нет"}"


achievement_1 = Achievement("Лыжный спорт", 2009, "Золото")

vasia = Athlete("Вася", 36, "Лыжный спорт", [], True)