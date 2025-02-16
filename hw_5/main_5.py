from abc import ABC, abstractmethod

# 1.1
class ATransport(ABC):
    def __init__(self, engine: str):
        self._engine = engine

    @abstractmethod
    def move(self): pass

class APublicTransport(ATransport):
    def __init__(self, engine, trip_price: int):
        self._trip_price = trip_price
        super().__init__(engine)

class APersonalTransport(ATransport):
    def __init__(self, engine):
        super().__init__(engine)


class Bus(APublicTransport):
    def __init__(self, engine, trip_price):
        super().__init__(engine, trip_price)

    def move(self):
        return "Автобус едет."

class Tram(APublicTransport):
    def __init__(self, engine, trip_price):
        super().__init__(engine, trip_price)

    def move(self):
        return "Трамвай едет."

class Taxi(APublicTransport):
    def __init__(self, engine, trip_price):
        super().__init__(engine, trip_price)

    def move(self):
        return "Такси едет."

class Motorbike(APersonalTransport):
    def __init__(self, engine):
        super().__init__(engine)

    def move(self):
        return "Мотоцикл едет."

class Scooter(APersonalTransport):
    def __init__(self, engine):
        super().__init__(engine)

    def move(self):
        return "Самокат едет."

class Car(APersonalTransport):
    def __init__(self, engine):
        super().__init__(engine)

    def move(self):
        return "Самокат едет."


# 1.2
class AFigure(ABC):
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @abstractmethod
    def show_figure(self): pass

class AXYFigure(AFigure):
    def __init__(self, x, y):
        super().__init__(x, y)

class AXYZFigure(AFigure):
    def __init__(self, x, y, z):
        self._z = z
        super().__init__(x, y)

class Circle(AXYFigure):
    def __init__(self, x, y):
        super().__init__(x, y)

    def show_figure(self):
        return "Круг!"

class Triangle(AXYFigure):
    def __init__(self, x, y):
        super().__init__(x, y)

    def show_figure(self):
        return "Треугольник!"

class Rectangle(AXYFigure):
    def __init__(self, x, y):
        super().__init__(x, y)

    def show_figure(self):
        return "Прямоугольник!"

class Ball(AXYZFigure):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def show_figure(self):
        return "Шар!"

class Cube(AXYZFigure):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def show_figure(self):
        return "Куб!"

class Pyramid(AXYZFigure):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def show_figure(self):
        return "Пирамида!"


# 2.1
class AFarmAnimal(ABC):
    def __init__(self, name: str):
        self._name = name

    @abstractmethod
    def eating(self, status: bool): pass

class Cow(AFarmAnimal):
    def __init__(self, name):
        super().__init__(name)

class Sheep(AFarmAnimal):
    def __init__(self, name):
        super().__init__(name)

class Chicken(AFarmAnimal):
    def __init__(self, name):
        super().__init__(name)

    def flying(self):
        return "Куропатка летает!"

class Pig(AFarmAnimal):
    def __init__(self, name):
        super().__init__(name)

class AFarmTransport(ABC):
    def __init__(self, case: str):
        self._case = case

    @abstractmethod
    def working(self, status: bool): pass

class Tractor(AFarmTransport):
    def __init__(self, case):
        super().__init__(case)

class Harvester(AFarmTransport):
    def __init__(self, case):
        super().__init__(case)

class AGrainCrop(ABC):
    def __init__(self, capacity: int):
        self._capacity = capacity

    @abstractmethod
    def content(self, status: bool): pass

class Greenhouse(AGrainCrop):
    def __init__(self, capacity):
        super().__init__(capacity)

class Storage(AGrainCrop):
    def __init__(self, capacity):
        super().__init__(capacity)


# 2.2
class Account:
    def __init__(self, card_number: int, cvv: int):
        self.__card_number = card_number
        self.__cvv = cvv

    @abstractmethod
    def money_to_state(self, cost: int):
        if DebitAccount.get_balance >= cost:
            DebitAccount.get_balance -= cost
            return "Успешно!"
        else:
            return "Недостаточно средств."

class BankClient(Account):
    def __init__(self, card_number, cvv, passport: int):
        self.__passport = passport
        super().__init__(card_number, cvv)

class CreditAccount(BankClient):
    def __init__(self, card_number, cvv, passport, anti_balance: int):
        self.__anti_balance = anti_balance
        super().__init__(card_number, cvv, passport)

class DebitAccount(BankClient):
    def __init__(self, card_number, cvv, passport, balance: int):
        self.__balance = balance
        super().__init__(card_number, cvv, passport)

class ATransaction(DebitAccount):
    def __init__(self, card_number, cvv, passport, balance):
        super().__init__(card_number, cvv, passport, balance)

    @abstractmethod
    def money_transfer(self, number: int): pass

class ATM(ATransaction):
    def __init__(self, card_number, cvv, passport, balance):
        super().__init__(card_number, cvv, passport, balance)

    def money_transfer(self, number: int):
        return "Транзакция через банкомат!"

class OnlineBaking(ATransaction):
    def __init__(self, card_number, cvv, passport, balance):
        super().__init__(card_number, cvv, passport, balance)

    def money_transfer(self, number: int):
        return "Транзакция через онлайн-банк!"

class ABankWorker(ABC):
    def __init__(self, name: str, stage: int):
        self._name = name
        self._stage = stage

    @abstractmethod
    def tea_time(self): pass

class Manager(ABankWorker):
    def __init__(self, name, stage):
        super().__init__(name, stage)

    def tea_time(self):
        return "Чаёк менеджеру!"


class Cashier(ABankWorker):
    def __init__(self, name, stage):
        super().__init__(name, stage)

    def tea_time(self):
        return "Чаёк кассиру!"